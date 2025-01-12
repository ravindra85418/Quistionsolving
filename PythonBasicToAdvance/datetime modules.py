import datetime
x=datetime.datetime.now()
print(x)

# using anlising modules through
import datetime as dt
x=dt.datetime.now()
print(x)

from datetime import *
x=datetime.now()
print(x)
print(x.year)
print(x.month)
print(x.day)
print(x.hour)
print(x.minute)
print(x.second)
print(x.microsecond)



from datetime import *
x=datetime(2025,1,1,12,15,20)
print(x)

# using strtime modules

from datetime import *
x=datetime.now()
print(x)
print(x.strftime('%A'))
print(x.strftime('%a'))
print(x.strftime('%Y'))
print(x.strftime('%y'))
print(x.strftime('%B'))
print(x.strftime('%b'))
