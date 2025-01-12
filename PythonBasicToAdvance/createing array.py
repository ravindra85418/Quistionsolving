from array import *
A=array('i',[])
n=int(input("enter length of array :"))
for i in range(n):
    x=int(input("enter valus:"))
    A.append(x)
    print(A)
s=int(input("enter the array element for search:"))
if s in A:
    print("the array element ",s,"present at the index:",A.index(s))
else:
    print("there is no",s,"element:")
