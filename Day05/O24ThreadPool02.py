
import concurrent.futures
from threading import current_thread
import time

"""
python ThreadPool
A thread pool is a collection of threads that are created in advance and can be reused to execute multiple tasks
ThreadpoolExecutor class that makes it easy to create and manage thread pool
"""

def display(index):
    num = 5
    print(f"{index} : Tid = {current_thread().name}")
    time.sleep(3)

def entry_point():
    tpool = concurrent.futures.ThreadPoolExecutor(max_workers=2)
    for n in range(5):
        tpool.submit(display, n + 1)
    tpool.shutdown(wait=True)
    print("Main Completed......")

if __name__ == '__main__':
    entry_point()

