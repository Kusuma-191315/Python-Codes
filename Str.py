a = [1, 2, 3]#list
b = a
c = [1, 2, 3]
print(a is b)
#is > address of  the memory
#== > content checks the content inside the string
print(a is c)
print(a == c)

s1 = "" #String datatype & Empty String
result  = bool(s1)
print(s1)
print(type(result)) #Output is Nul bcs its empty

s1 = " " # string with space (string in python with character is always true)
         # but an empty string with no character will retuen always false
result = bool(s1)
print(s1)
print(type(result))