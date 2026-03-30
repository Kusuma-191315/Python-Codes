#code for 3rows and 5 colums *
rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of column: "))
for i in range(rows):
    for j in range(columns):
        print('*', end=' ')
    print()

#code for right angle triangle
rows = int(input("Enter number of rows: "))
for i in range(rows):
    for j in range(i):
        print('*', end=' ')
    print()

#hallow rectanngle pattern(just border rectangle)
rows = int(input("Enter number of rows:"))
columns = int(input("Enter the number of column:"))
for i in range(rows):
    if i == 0 or i == rows - 1:  #it print the top or bottom boredr of the rectangle
        print('*' * columns)
    else: # print the middle  rows with spaces in between
        print('*' + ' ' * (columns - 2) + '*')


#for large  rectangle
rows = int(input("Enter number of rows:"))
for i in range(rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()

# small rect
rows = int(input("Enter number of rows:"))
columns = int(input("Enter number of columns:"))
for i in range(rows):
    for j in range(columns):
        print("*", end=" ")
    print()