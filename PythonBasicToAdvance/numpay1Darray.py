# creating single dimensional array by accepting elements at run time with NumpyArray

from numpy import *
n = int(input("enter the size of array :"))
A = ndarray(shape=(n,),dtype=int)

for i in range(n):
    x = int(input("enter array elements:"))
    A[i] = x
print(A)
