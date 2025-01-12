# what is *args and **kwargs
def add(*args):
    s=0
    for i in args:
        print("sum is :",s)
add(10,20)
add(2,3,4)
add(10,20,30,40,50,60,70)


# **kwargs

def f1 (**kwargs):
    print(kwargs)
    for k,v in  kwargs.items():
        print(k,"=",v)
f1(a=10,b=20,c=30)
f1(eid=1234,ename="ravinder",eaddress="fuljhariya",esal=71500)

