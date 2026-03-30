# Multiple line comment
s = """Hello ,
    How are you?
    Thank You!"""
print(s)

# Understandingg the concept of String is immutable 
#  simple Example 1
s1 ="Hello" 
s1 = s1+("World")
print(s1) 

# Example 2
s1 = "python"
s2 = "python" 
print(s1, id(s1))
print(s2, id(s2))
print(s1 is s2)

# Example 3 (false because Pis caps in s1 though python is case sensitive it gives o/p false)
s1 = "Python"
s2 = "python" 
print(s1, id(s1))
print(s2, id(s2))
print(s1 is s2)

# Example 3
s1 = "Hello"
s2 = s1+("world")
print(s1, id(s1))
print (s2, id(s1))