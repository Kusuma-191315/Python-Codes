# use curly braces 
st = {10, 30.45, 4+6j, "Kusu", True}
print(st)
print(type(st))
#set is immutable it cant change 
#set don't allow duplicate value
#set doesn't support index value 

#To add element to set down code
st.add(60)
print(st)

#to remove element 
st.remove(30.45)
print(st)

#using pop without index value but its not gonna remove order wise but it will remive any 1 elemet
st.pop()
print(st) # remove any 1 element 

st.pop() # remove another element
print(st)

#---------------------------#
str1 = {10, 20, 30, 40, 50}
print(str1)

str2 = {40, 50, 60, 70, 80}
print(str2)

u_set = str1.union(str2) # combine 2 set and put in onewe use union set
print(u_set) # it do not repeat element 

#----------------------------#
#intersection (commom elelement display)
i_set = str1.intersection(str2)
print(i_set)


#update function (display current element fron both side and can add extra element)
str1.update(str2)
print(str1)