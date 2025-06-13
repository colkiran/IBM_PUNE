
import time

def doJob():
    print("Job Started...")
    time.sleep(2)
    print("Job completed.....")

st = time.perf_counter()
doJob()
doJob()
doJob()
et = time.perf_counter()

print(f"Total time taken to execute :{round(et - st, 2)}")