#greeting
def greet():
    print("Hello! Welcome")
greet()

#adding 2 numbers

def add():
    a = 10
    b = 20
    print(a+b)
add()

#find sqaur of a number
def square():
    a = 5
    b = 3
    print(a*a)
    print(b*b)
square()

#find largest of 3 numbers
def large():
    a, b, c = 2, 5, 9
    print(max(a, b,c))
large()

#smallest
def small():
    p, q, r = 8, 12, 19
    print(min(p, q, r))
small()

#larger code for Largest 3 number
def largenum():
    a=36
    b=45
    c=34
    if(a>b and a>c):
        print(a)
    elif(b>a and b>c):
        print(b)
    else:
        print(c)
largenum()