def f1():
    print("hello")
    def f2():
        print("hai")
        def f3():
            print("welcome")
        f3()
    f2()
f1()