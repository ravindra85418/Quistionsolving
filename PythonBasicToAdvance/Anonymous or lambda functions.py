# lambda function to find square of number
s=lambda n:n*n
print(s(4))
#
# lambda function find sum of two numbers
s=lambda a,b:a+b
print(s(10,20))


# lambda function to find biggest of two numbers
s=lambda a,b: a if a>b else b
print(s(34,56))

# lambda function to find biggest of 3 numbers
s=lambda a,b,c: a if a>b and a>c else b if b>c else c
print(s(2,3,5))


# lambda function to find number is even or odd
s=lambda n: "is even" if n%2==0 else "is odd"
print(s(5))
print(s(8))