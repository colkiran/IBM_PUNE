

import time
from threading import Thread, current_thread

def doJob():
    print(f"Job Started... {current_thread().name}")
    time.sleep(2)
    print(f"Job completed.....{current_thread().name}")

st = time.perf_counter()
t1 = Thread(target=doJob, name="thrd-1")
t2 = Thread(target=doJob, name="thrd-2")
t3 = Thread(target=doJob, name="thrd-3")


t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

et = time.perf_counter()


print(f"Total time taken to execute :{round(et - st, 2)}")
