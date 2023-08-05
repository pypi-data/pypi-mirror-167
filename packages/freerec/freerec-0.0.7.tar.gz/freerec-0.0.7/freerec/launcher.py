

from typing import Callable, List, Dict, Optional

import torch
import os
from functools import partial
from collections import defaultdict
from tqdm import tqdm
import pandas as pd

from .data.datasets.base import BaseSet
from .data.fields import Field, Fielder
from .data.dataloader import DataLoader
from .dict2obj import Config
from .utils import AverageMeter, Monitor, timemeter, infoLogger
from .metrics import *


__all__ = ['Coach']


DEFAULT_METRICS = {
    'LOSS': None,
    #############
    'MSE': mean_squared_error,
    'MAE': mean_abs_error,
    'RMSE': root_mse,
    #############
    'PRECISION': precision,
    'RECALL': recall,
    'HITRATE': hit_rate,
    #############
    'NDCG': normalized_dcg,
    'MRR': mean_reciprocal_rank,
    'MAP': mean_average_precision
}

DEFAULT_FMTS = {
    'LOSS': ".5f",
    #############
    'MSE': ".4f",
    'MAE': ".4f",
    'RMSE': ".4f",
    #############
    'PRECISION': ".4f",
    'RECALL': ".4f",
    'HITRATE': ".4f",
    #############
    'NDCG': ".4f",
    'MRR': ".4f",
    'MAP': ".4f",
}

DEFAULT_BEST_CASTER = {
    'LOSS': min,
    #############
    'MSE': min,
    'MAE': min,
    'RMSE': min,
    #############
    'PRECISION': max,
    'RECALL': max,
    'HITRATE': max,
    #############
    'NDCG': max,
    'MRR': max,
    'MAP': max,
}

class _DummyModule(torch.nn.Module):

    def forward(self, *args, **kwargs):
        raise NotImplementedError("No available model is provided for Coach ...")

    def step(self, *args, **kwargs):
        raise NotImplementedError("No available optimizer or lr scheduler is provided for Coach ...")

    def backward(self, *args, **kwargs):
        raise NotImplementedError("No available optimizer is provided for Coach ...")


class Coach:
    
    def __init__(
        self, 
        dataset: BaseSet,
        criterion: Callable,
        model: Optional[torch.nn.Module],
        optimizer: Optional[torch.optim.Optimizer],
        lr_scheduler: Optional[torch.optim.lr_scheduler._LRScheduler],
        device: torch.device
    ):
        self.dataset = dataset
        self.fields: Fielder[Field] = self.dataset.fields
        self.device = device
        self.criterion = criterion
        self.model = model if model else _DummyModule()
        self.optimizer = optimizer if optimizer else _DummyModule()
        self.lr_scheduler = lr_scheduler if lr_scheduler else _DummyModule()

      
    def save(self) -> None:
        torch.save(self.model.state_dict(), os.path.join(self.cfg.INFO_PATH, self.cfg.SAVED_FILENAME))

    def save_checkpoint(self, epoch: int) -> None:
        path = os.path.join(self.cfg.INFO_PATH, self.cfg.CHECKPOINT_FILENAME)
        checkpoint = dict()
        checkpoint['epoch'] = epoch
        for module in self.cfg.CHECKPOINT_MODULES:
            checkpoint[module] = getattr(self, module).state_dict()
        checkpoint['monitors'] = self.monitors.state_dict()
        torch.save(checkpoint, path)

    def load_checkpoint(self) -> int:
        path = os.path.join(self.cfg.INFO_PATH, self.cfg.CHECKPOINT_FILENAME)
        checkpoint = torch.load(path)
        for module in self.cfg.CHECKPOINT_MODULES:
            getattr(self, module).load_state_dict(checkpoint[module])
        self.monitors.load_state_dict(checkpoint['monitors'])
        return checkpoint['epoch']

    def save_best(self, path: str, prefix: str): ...

    def check_best(self, val: Optional[float]): ...

    @timemeter("Coach/resume")
    def resume(self):
        start_epoch = self.load_checkpoint() if self.cfg.resume else 0
        infoLogger(f"[Coach] >>> Load the recent checkpoint and train from epoch: {start_epoch}")
        return start_epoch

    @property
    def monitors(self) -> Monitor:
        """Dict[str, Dict[str, List]]
        Monitor[prefix: str, Dict[metric: str, meters: List]]
        """
        return self.__monitors

    @timemeter("Coach/compile")
    def compile(
        self, cfg: Config, monitors: List[str]
    ):
        self.cfg = cfg
        # meters for train|valid|test
        self.__monitors = Monitor()
        self.__monitors['train'] = {
            'LOSS': [
                AverageMeter(
                    name='LOSS', 
                    metric=DEFAULT_METRICS['LOSS'], 
                    fmt=DEFAULT_FMTS['LOSS']
                )
            ]
        }
        self.__monitors['valid'] = defaultdict(list)
        self.__monitors['test'] = defaultdict(list)

        for name in monitors:
            name = name.upper()
            if '@' in name:
                metric, K = name.split('@')
                for prefix in ('valid', 'test'):
                    self.__monitors[prefix][metric].append(
                        AverageMeter(
                            name=name,
                            metric=partial(DEFAULT_METRICS[metric], k=int(K)),
                            fmt=DEFAULT_FMTS[metric]
                        )
                    )
            else:
                metric = name
                for prefix in ('valid', 'test'):
                    self.__monitors[prefix][metric].append(
                        AverageMeter(
                            name=name,
                            metric=DEFAULT_METRICS[metric],
                            fmt=DEFAULT_FMTS[metric]
                        )
                    )

        # dataloader
        self.load_dataloader()

    def load_dataloader(self):
        self.__dataloader = DataLoader(
            datapipe=self.dataset, num_workers=self.cfg.num_workers
        )
    
    @property
    def dataloader(self):
        if self.cfg.verbose:
            return tqdm(
                self.__dataloader,
                leave=False, desc="վ'ᴗ' ի-"
            )
        else:
            return self.__dataloader

    def monitor(
        self, *values,
        n: int = 1, mode: str = 'mean', 
        prefix: str = 'train', pool: Optional[List] = None
    ):
        metrics: Dict[List] = self.monitors[prefix]
        for metric in pool:
            for meter in metrics.get(metric, []):
                meter(*values, n=n, mode=mode)

    def step(self, epoch: int):
        for prefix, metrics in self.monitors.items():
            metrics: Dict[str, List[AverageMeter]]
            infos = [f"[Coach] >>> {prefix.upper():5} @Epoch: {epoch:<4d} >>> "]
            for meters in metrics.values():
                infos += [meter.step() for meter in meters if meter.active]
            infoLogger(' || '.join(infos))

    @timemeter("Coach/summary")
    def summary(self):
        file_ = os.path.join(self.cfg.LOG_PATH, self.cfg.SUMMARY_FILENAME)
        s = "|  {prefix}  |   {metric}   |   {val:.5f}   |   {epoch}   |   {img}   |\n"
        info = ""
        info += "|  Prefix  |   Metric   |   Best   |   @Epoch   |   Img   |\n"
        info += "| :-------: | :-------: | :-------: | :-------: | :-------: |\n"
        data = []

        for prefix, metrics in self.monitors.items():
            metrics: defaultdict[str, List[AverageMeter]]
            freq = 1 if prefix == 'train' else self.cfg.EVAL_FREQ
            for METRIC, meters in metrics.items():
                for meter in meters:
                    meter.plot(freq=freq)
                    imgname = meter.save(path=self.cfg.LOG_PATH, prefix=prefix)
                    epoch, val = meter.argbest(DEFAULT_BEST_CASTER[METRIC], freq)
                    info += s.format(
                        prefix=prefix, metric=meter.name,
                        val=val, epoch=epoch, img=f"![]({imgname})"
                    )
                    data.append([prefix, meter.name, val, epoch])

        with open(file_, "w", encoding="utf8") as fh:
            fh.write(info) # Summary.md

        df = pd.DataFrame(data, columns=['Prefix', 'Metric', 'Best', '@Epoch'])
        infoLogger(str(df)) # print final metrics
        # save corresponding data for next analysis
        self.monitors.save(self.cfg.LOG_PATH, self.cfg.MONITOR_FILENAME)


    def train_per_epoch(self):
        raise NotImplementedError()

    def evaluate(self, prefix: str = 'valid'):
        raise NotImplementedError()


    @timemeter("Coach/train")
    def train(self):
        self.dataset.train()
        self.model.train()
        return self.train_per_epoch()

    @timemeter("Coach/valid")
    @torch.no_grad()
    def valid(self):
        self.dataset.valid() # TODO: multiprocessing pitfall ???
        self.model.eval()
        return self.evaluate(prefix='valid')

    @timemeter("Coach/test")
    @torch.no_grad()
    def test(self):
        self.dataset.test()
        self.model.eval()
        return self.evaluate(prefix='test')

    @timemeter("Coach/fit")
    def fit(self):
        start_epoch = self.resume()
        for epoch in range(start_epoch, self.cfg.epochs):
            if epoch % self.cfg.CHECKPOINT_FREQ == 0:
                self.save_checkpoint(epoch)
            if epoch % self.cfg.EVAL_FREQ == 0:
                if self.cfg.EVAL_VALID:
                    self.check_best(self.valid())
                if self.cfg.EVAL_TEST:
                    self.test()
            self.train()

            self.step(epoch)
        self.save()

        # last epoch
        self.check_best(self.valid())
        self.test()
        self.step(self.cfg.epochs)

        self.summary()


class CoachForCTR(Coach): ...

class CoachForMatching(Coach): ...