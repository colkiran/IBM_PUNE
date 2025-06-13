
import time
from threading import Thread, current_thread

def doJob(secs, tname):
    print(f"Job Started... {tname}")
    time.sleep(secs)
    print(f"Job completed.....{tname}")

st = time.perf_counter()

threads = []

for i  in range(50):
    t = Thread(target=doJob, name="thrd-"+str(i), args=(2, "thrd-"+str(i)))
    t.start()
    # t.join()    # the next thread will start after completing the join of the current thread
    threads.append(t)

for thread in threads:
    thread.join()

et = time.perf_counter()


print(f"Total time taken to execute :{round(et - st, 2)}")
