fruit_name = ["apple", "mango", "banana"] #fruit_name is variable
print(fruit_name)
print(fruit_name[2])
print(fruit_name[0])
print(fruit_name[1])

vegetable_name = ["carrot", "beans", "potato", "potato"] # cheking duplicate value will execute or not
print(vegetable_name)
#output will be same because python allow duplicate value in list
#and this is also a homogeneous datatype bcs its allow same type of data and the data is string type

fav_list = ["Sachin", 10, 3.14, 31+6j, False]
print(fav_list)
#it allow heterogenous data also


#down code shows that list is mutable(changeable)
fav_hobby = ["singing", "danceing", "cooking"]
print(fav_hobby)

fav_hobby[2] = "Watching series"
print(fav_hobby)

#adding extra/new to list(append)
fav_hobby.append("eating")#adding extra/new element to list
print(fav_hobby)

#remove old elemet(remove)
fav_hobby.remove("singing")#removing singing from list
print(fav_hobby)

#removing using index number (delete / del)
del fav_hobby[2] #deleting using index number
print(fav_hobby)

fruits = ["Apple", "Mango", "Banana", "Banana"]
print(fruits.index("Banana"))
print(fruits.count("Banana"))