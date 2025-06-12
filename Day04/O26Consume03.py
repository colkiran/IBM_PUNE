
import sys

# env path
# print(sys.path)

sys.path.append("C:\\Delhi")

for path in sys.path:
    print(path)


from gurgaon.mymodule import greet

print("-" * 60)
greet("Rahul Dravid")
