#Arthematic Operators
a = 10
b =2

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("floor Division:", a // b)
print("Modulus:", a % b)
print("Power:", a ** b)

#Comparision Operator
x = 5
y = 10

print("x > y :", x > y)
print("x < y :", x < y)
print("x == y :", x == y)
print("x != y :", x != y)
print("x >= y :", x >= y)
print("x <= y :", x <= y)

#Logical Operator 
p = True
q = False

print("p and q :", p and q)
print("p or q :", p or q)
print("not p :", not p)
print("not q :", not q)

#Assignmanet Operator
num = 10
print("Initial value:", num)

num += 5
print("After += :", num)

num -= 3
print("After -= :", num)

num *= 2
print("After *= :", num)

num //= 4
print("After //= :", num)

#Identity Operator
a = 5
b = 5
c = 10
print("a is b:", a is b)
print("a is c:", a is c)
print("a is not c:", a is not c)

#Memebershiop Operator
number = [1, 2, 3, 4, 5]
print("3 in list :", 3 in number)
print("10 in list :", 10 in number)
print("10 not in list :", 10 not in number)

#Bitwise Operator
a = 5
b = 3
print(a & b)# bitwise and
print(a | b)# bitwise or
print(a ^ b)# bitwise Xor
print(a << b)#bitwise leftshift
print(a >> b)#bitwise rightshift
print(~a)
print(~b)