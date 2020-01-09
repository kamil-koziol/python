from contextlib import contextmanager
import time

@contextmanager
def calc_time():
    try:
        start=time.perf_counter()
        yield
    finally:
        print(time.perf_counter() - start)

with calc_time():
    for i in range(1000):
        pass