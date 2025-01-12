# without lambda
def dbl(x):
    return 2*x


l=[2,3,4,5,6,7,8,9,10]
l1=list(map(dbl,l))
print(l1)

# with lambda
l=[2,3,4,5,6,7,8,9,10]
l1=list(map(lambda x:2*x,l))
print(l1)


l1=[2,3,4,5,7]
l2=[5,6,7,8,9]
l3=list(map(lambda x,y:x+y,l1,l2))
print(l3)
