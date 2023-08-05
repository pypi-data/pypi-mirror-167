



from typing import TypeVar, Callable

T = TypeVar('T')

def safe_cast(val: T, dest_type: Callable[[T], T], default: T) -> T:
    try:
        if val:
            return dest_type(val)
        else: # fill_na
            return default
    except ValueError:
        raise ValueError(f"Using '{dest_type.__name__}' to convert '{val}' where the default value is {default}")