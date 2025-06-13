
import time
from concurrent.futures import  ThreadPoolExecutor

def doJob(val):
    print("Job Started.....")
    time.sleep(2)
    print("Job Completed......")
    val += val
    return val

pool = ThreadPoolExecutor(2)

t1 = pool.submit(doJob, 5)
t2 = pool.submit(doJob, 6)
t3 = pool.submit(doJob, 4)
t4 = pool.submit(doJob, 8)
t5 = pool.submit(doJob, 6)

if t3.done():
    print(t3.result())
else:
    print("Yet to calculate")

time.sleep(6)

if t3.done():
    print(t3.result())

t6 = pool.submit(doJob, 6)
t7 = pool.submit(doJob, 4)
t8 = pool.submit(doJob, 8)
t9 = pool.submit(doJob, 6)

# print("Hello World")
pool.shutdown()

t10 = pool.submit(doJob, 6)