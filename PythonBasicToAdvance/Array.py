import array
A=array.array( 'i',  [10,20,30,40])
print(A)
print(type(A))

import array as arr
A=arr.array('i',[10,20,30,40])
print(A)
print(type(A))


from array import *
A=array('i',[10,20,30,40])
print(A)
print(type(A))
print(A.typecode)
A.remove(20)
print(A)