class Test:
    a=10  #ststic variables
    def __init__(self):
        print("Inside the constructor")
        print(self.a)
        print(Test.a)
    def m1(self):
        print("Inside the instance methods")
        print(self.a)
        print(Test.a)

    @classmethod
    def m2(cls):
        print("Inside of class methods")
        print(cls.a)
        print(Test.a)

    @staticmethod
    def m3():
     print("Inside of ststic methids")
     print(Test.a)
t=Test()
t.m1()
t.m2()
t.m3()
print("Outsideof the class")
print(Test.a)
print(t.a)


