#No arguemnet + No return value
def add():
    a = 10
    b = 20
    print(a+b)
add()

#No Arguement + Return value
def add():
    c = 5
    d = 45
    return c+d
print(add())

#Arguement + No return value
def add(x, y):
    print(x+y)
add(100, 200)

#Arguement + Return value
def add(p, q):
    return p+q
res = add(200, 300)
print(res)

#Finding cube using function methods
def cube():  #this is with No arguement and No return value
    a = 2
    print(a*a*a)
cube()

def cube(): # this is with No arguement and with return value
    a=5
    return a*a*a
print(cube())

def cube(a): # this is with Arguement and No return value
    a=3
    print(a*a*a)

def cube(a): #this is with Arguement and Retuen value
    return(a*a*a)
res = cube(4)
print(res)