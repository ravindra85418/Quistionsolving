def f1 (*a):
    print(a)
f1()
f1(10)
f1(10,20)
f1(10,10,30,50)




# adding n nobs of variable length arguments
def add(*n):
    s=0
    for i in  n:
        s=s+i
        print("sum is:",s)
add(10,20)
add(2,3,4)
add(2,3,4,5,6,7)
add(10,20,30,40,50,60,70)
