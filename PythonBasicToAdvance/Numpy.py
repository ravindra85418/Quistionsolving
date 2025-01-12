# Numpy methods:
# 1.array()
# 2.linespace()
# 3.Logspace()
# 4.Arange()
# 5.Zeros()
# 6.Ones()


# 1.array()
import numpy
A=numpy.array([10,20,30,40,50.8],int)
print(A)
print(type(A))
print(A.dtype)
print(A.ndim)
print(A.size)
print(A.shape)

# 2.Linespace()
from numpy import *
A= linspace(2,20,7)
print(A)
A= logspace(3,15,6)
print(A)
A=arange(2,10,3)
print(A)
A= zeros(6,int)
print(A)
A= ones(6,int)
print(A)
