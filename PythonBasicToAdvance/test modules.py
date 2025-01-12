# using simple.py function

import simple

print(simple.a)
simple.add(10,20)
simple.sub(50,30)



# modules alising:-change other nsme to modules is called module alising
# ex:-simple name change=simple as sm


import simple as sm
print(sm.a)
sm.add(20,50)
sm.sub(10,25)



from simple import*
print(a)
add(10,20)
sub(20,10)



from simple import a,add,sub
print(a)
add(20,30)
sub(50,30)



# member alising modules
import simple
import simple1
print(a)
simple.add(20,30)
simple.sub(5,2)
print(a)
simple1.multi(5,2)





from simple import *
from simple1 import *
print(a)
add(53,12)
sub(25,20)
print(a)
multi(25,3)


# a value isreprinting then 2 line import line are print

from simple import *
print(a)
add(20,31)
sub(45,20)
from simple1 import *
print(a)
multi(45,3)
