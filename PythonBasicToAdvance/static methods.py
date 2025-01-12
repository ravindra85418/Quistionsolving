class student:
    name= "Ravindra"    #static variale & class level
    def __init__(self,m1,m2,m3): #constructer
        self.m1=m1
        self.m2= m2
        self.m3=m3
    def avg(self):     #instance methods
        print((self.m1+self.m2+self.m3)/3)

    @classmethod
    def m1(cls):  #class methods
     print(cls.name)

    @staticmethod
    def add(a,b):     #static methods
        print("sum is:",a+b)


    @staticmethod
    def f1():
        print("hello")

s1=student(78,87,69)
s2=student(90,86,94)
s1.avg()  #object refrence out side of the class
s2.avg()
student.m1()
s1.add(10,20)
s1.f1()
