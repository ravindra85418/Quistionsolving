def f1():
    print("hello")
f2=f1
# del f1
f2()
print(id(f1))
print(id(f2))

