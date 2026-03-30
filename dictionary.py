#example for dic
student = {
 "name": "kusu" , #key is name and kusu is value
 "age": 21,
 "course": "BCA", 
}
print(student)
print(type(student))

#access value
print(student["name"])
print(student.get("age"))

#update / add value
student["age"] = 22
student["city"] = "Delhi"

#remove element
student.pop("age") # remove age
del student["course"] # deletes course
student.clear() #removes all items

#looping in dict

for key in student:
    print(key, student[key])
for key, value in student.items():
    print(key, value)

#usefull methods 
student.keys() #return all key
student.values()  # all values
student.items() # returns keu-value pairs

#simple exmp program 
marks = { 
    "Math":  90,
    "Scienece": 85,
    "English": 100
}
total = 0
for subject, score in marks.items():
    total += score
print("Total Marks:", total)
print("Average:", total / len(marks))

#using get()
d = {"name": "Rahul", "age": 21}
print(d.get("name"))
print(d.get("city"))
print(d.get("city", "NA"))