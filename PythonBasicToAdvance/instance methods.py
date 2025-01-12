class student:
    def __init__(self,m1,m2,m3): #constructer
        self.m1=m1
        self.m2= m2
        self.m3=m3
    def avg(self):     #instance method
        print((self.m1+self.m2+self.m3)/3)
s1=student(20,30,45)
s2=student(45,85,65)
s1.avg()  #object refrence out side of the class
s2.avg()
