class Student:
    def __init__(self,x,y,z):
        self.sid=x
        self.sname=y
        self.saddress=z

    def display(self):
        print("student id is :",self.sid)
        print("student name is :",self.sname)
        print("student assress is :",self.saddress)
s1=Student(101,"sai","hydrabad")
s2=Student(102,"mohan","bhopal")
s1.display()
s2.display()