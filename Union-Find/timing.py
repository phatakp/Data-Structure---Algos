from functools import wraps
import time


def timing(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        tic = time.perf_counter()
        value = func(*args, **kwargs)
        toc = time.perf_counter()
        elapsed = toc - tic
        print(f'Elapsed time: {elapsed} seconds')
        return value
    return wrapper
