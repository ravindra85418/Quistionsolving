class outer:
    def __init__(self):
        print("Outer classs consructor")
    def f1(self):
        print("outer class methods")
    class Inner:
        def __init__(self):
         print("Inner class constructor")
        def m1(self):
         print("Inner class methods")
o=outer()
o.f1()
i=o.Inner()
i.m1()