# special varibles__name__ modules
def f1():
    if __name__=='__main__':
        print("executing as an individual program")
    else:
        print("executed from some other program")
f1()
print(__name__)




