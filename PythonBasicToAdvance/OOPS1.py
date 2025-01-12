# To display student details without constructor

class Student:
    def getdata(self):
        self.sid=int(input("enter sid:"))
        self.sname=input("enter sname:")
        self.saddress=input("enter saddress:")
    def display(self):
        print("student id id:",self.sid)
        print("student name is:",self.sname)
        print("enter address id:",self.saddress)
s1=Student()
s1.getdata()
s1.display()
