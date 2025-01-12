import time

class Test:
    def __init__(self):
        print("constructor execusion")
    def __dir__(self):
        print("destructor execusion")
t=Test()
time.sleep(5)
print("End of the program")
