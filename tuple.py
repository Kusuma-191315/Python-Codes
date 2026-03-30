t = (1, 2, 3)#homogeneous type
print(type(t))

#index  0   1   2      3
t1 = (3.4, 4, "Kusu", True)#heterogeneoustype
#- index -4    -3    -2       -1
print((t1))
print(t1[2])
print(t1[3])
print(t1[-2]) 

t2 = (4)#giving single value by asking type
print(type(t2))#imposible because its a tuple type but its showing int type or string type as it is ....

#--------if want single value--------#
t2=(4, )#give , after single value 
print(type(t2))

#============== tuple slicing ============#
t = (1,3,6,8,9,0)
print(t[1:4])#3 6 8 
print(t[:3])# 1 3 6


#operation/function
tup = (1, 2, 3 ,4) * 2
print(tup)#len
print(len(tup))

print(t1 + tup)

t3=(4, ) * 3# to repear 3 times
print(t3)

#return type in python
def name():# using tuple we can return multiple value 
    n1 = "Kusu"
    n2 = "Chandhu"
    n3 = "Dacchu"
    n4 = "Shivi"
    return (n1, n2, n3, n4)
print(name())

#packing in tuple
student = ("Kusuma", 21, "Kannada")
print(student)

#unpacking in tuple
name, age, subject = student
print(name)
print(age)
print(subject)