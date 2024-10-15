'''
    There are mainly three types of datatypes available in python
    Numeric, Sequence and Others (Collections)

    Numeric - int, float and complex
    Sequence - strings, List and Tuple (ordered and have index)
    Others - Boolean, Set and Dictionaries
    Collections - string, List, Tuple, Set and Dictionary

    Constant is a types of variable whose value cannot be changed
    Python does not have builtin constant types, but by convention,
    the variable name with all capital letters used to define a constant
'''

x = 10         # this is int
y = 10.3       # this is float
z = 10+4j      # this is complex
a = "Hi Ram"   # this is string
b = 'Hi Ram'   # this is string
c = True       # this is boolean
d = False      # this is boolean
FILE_SIZE_LIMIT = 200   # this we assume is a constant
PI_VALUE = 3.14  # this we assume is a constant

print(x)
print(y)
print(z)
print(a)
print(b)
print(c)
print(d)
print(x, z)

print(type(x))
print(type(y))
print(type(z))
print(type(a))
print(type(b))
print(type(c))
print(type(d))

print(type(10))
print(type(10.5))
print(type(10.5j))
print(type("Hi Ram"))
print(type('Hi Ram'))
print(type(True))
print(type(False))

xtype = type(x)
ytype = type(y)
ztype = type(z)
atype = type(a)
btype = type(b)
ctype = type(c)
dtype = type(d)
print(xtype)
print(ytype)
print(ztype)
print(atype)
print(btype)
print(ctype)
print(dtype)

num1, num2, num3 = 20, 30, 40
print(num1)
print(num1, num2, num3)

age1 = age2 = age3 = 30
print(age2)
print(age1, age2, age3)

name1, name2 = "Ram", "Bhumireddy"
print(name1, name2)
name2, name1 = name1, name2
print(name1, name2)

# id is the memory location where the value is stored for the variable
id1, id2, id3 = 100, 100, 200
print(id(id1))
print(id(id2))
print(id(id3))

del id1    # delete a variable from memory and also its value if it is not referencing in any other variable
