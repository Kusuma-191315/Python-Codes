#jump control statement
#break control statement  1-6 break = 3
for i in range(1, 6):
    if i == 4:
        break
    print(i)#123

#continue control statement
for i in range(0, 6):
    if i == 4: #skip
        continue
    print(i)#01235

#return control statement
def square(n):
    return n * n
print(square(4))

#pass control statement
for i in range(0, 6):
    pass


def add():
    pass
    add()