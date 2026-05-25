my_set = {1,2,3,4}
print(my_set)

#using set function
another_set = set([1,2,2,])
print(another_set)#remove duplicate value gives o/p as 1,2,3

#add function
s = {1,2,3}
s.add(4)
print(s)

s.remove(4)#remove function
print(s)
s.discard(5)#remove 
print(s)

#check Membership function
print(3 in s)#true

#set operation
#union (combine sets)
a = {1,2,3}
b = {3,4,5}
print(a|b) #12345

#intersection (commom/repeated element)
print(a&b) #3

#Difference (elements in a but not in b)
print(a-b)  #1,2

#symmetric difference (not commom)
print(a^b) #1245

#loop through in set
for item in a:
    print(item)
for item in b:
    print(item)

#removing duplicate value in the list
numbers = {1,2,2,3,4,4,5}
unique_numbers = set(numbers)
print(unique_numbers) 

#update 
a = {1,2}
a.update([3,4,5])
print(a)

#frozen set makes set immutable
fs = frozen_set = ([1,2,3])
print(fs)