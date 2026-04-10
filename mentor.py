# square og numbers without comprehension
sqr = [1,2,3,4,5]
new_sqr = []
for n in sqr:
    new_sqr.append(n*n)
print(new_sqr)

#with 
lcnew_sqr = [n * n for n in sqr]
print(lcnew_sqr)

#odd number without comprehensision
numbers = [1,2,3,4,5,6,7,8,9,10]
odd_number = []
for num in numbers:
    if num % 2 != 0:
        odd_number.append(num)
print(odd_number)

#with
lcodd_numbers = [num for num in numbers if num % 2 != 0]
print(lcodd_numbers)


#convert string to uppercase without  com
names = ["kusu", "chandhu", "dacchu"]
upper_names = []
for name in names:
    upper_names.append(name.upper())
print(upper_names)
#with
lcupper_names = [name.upper() for name in names]
print(lcupper_names)

#replace -ve number with 0 without com
negnumber = [1,2,-3,4,-6]
result = []
for num in negnumber:
    if num < 0:
        result.append(0)
    else:
        result.append(num)
print(result)

#with 
result = [0 if num < 0 else num for num in numbers]
print(result)

#length of each world without com
words = ["apple", "mango", "banana"]
lengths = []
for world in words:
    lengths.append(len(world))
print(lengths)

#with
lengths = [len(word) for word in words]
print(lengths)


