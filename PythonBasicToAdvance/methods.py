class Student:
    def __init__(self,x,y,z):
        self.sid=x
        self.sname=y
        self.saddress=z
s1=Student(101,"sai","hydrabad")
s2=Student(102,"mohan","bhopal")
print(s1.__dict__)
print(s2.__dict__)
