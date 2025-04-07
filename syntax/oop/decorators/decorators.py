import functools
import time
from functools import cache


def time_of_function(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print(f'Работа заняла {t2 - t1} секунд')
        return result

    return wrapper


@cache
@time_of_function
def func_one(a, b):
    """Return a friendly greeting."""
    my_list = [i for i in range(1, 100_000_000)]
    return a + b
