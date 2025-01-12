class parent:
    x=10
    _y=20
    __z=30
class Child(parent):
    print(parent.x)
    print(parent._y)
    print(parent.__z)

c=Child()
