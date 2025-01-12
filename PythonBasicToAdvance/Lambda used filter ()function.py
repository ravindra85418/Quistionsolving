# without lambda check a no is even or odd
def iseven(x):
    if x%2 ==0:
       return True
    else:
        return False

l=[1,2,3,4,5,6,7,8,9,10]
l1=list(filter(iseven,l))
print(l1)


# with lambda cheak a no is even or odd
L=[1,2,3,4,5,6,7,8,9,10]
L1=list (filter(lambda x:x%2==0,L))
print(L1)

