# reduce function not avaible defult
# without lambda
from functools import reduce
def f1 (x,y):
    return x+y


l=[10,20,30,40,50,60,70]
result=reduce(f1,l)
print(result)

# with lambda
l=[10,20,30,40,50,60,70]
result=reduce(lambda x,y:x+y,l)
print(result)