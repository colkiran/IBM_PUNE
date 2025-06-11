
from memory_profiler import profile

@profile
def fun(list_size):
    lst1 = ["hello"] * list_size
    lst2 = ["hello world"] * list_size
    del lst2
    return lst1

fun(1000000)
