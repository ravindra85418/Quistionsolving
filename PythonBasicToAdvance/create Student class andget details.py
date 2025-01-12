class Student:
    def get_student_details(self):
        self.sid=123
        self.sname="ravi"
        self.saddress="bihar"
        self.sage=26

    def display_student_details(self):
        print("student id:",self.sid)
        print("student name:",self.sname)
        print("student age:",self.saddress)
        print("student age:",self.sage)
s=Student()
s.get_student_details()
s.display_student_details()   

