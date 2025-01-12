class Test:
    x=10
    _y=20
    __z=30
    def __init__(self):
        print("within the class")
        print(self.x)
        print(self._y)
        print(self.__z)
t=Test()
print("Outside of the class")
print(t.x)
print(t._y)
print(t.__z)
