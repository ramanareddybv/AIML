'''
    Type conversion is an act of changing an object's data type
    Python defines type conversion functions to directly convert one data type to another
    which is useful in daya-to-day and competitive programming
    The python interpreter automatically performs Implicit Type Conversion
    At the same time, Python prevents Implicit Type Conversion from losing data

    There are two types of Type Conversion in Python
        - Implicit Type Conversion
        - Explicit Type Conversion

    Type Casting
        Type casting is a process of explicit type conversion
        Here the user converts the data types of objects using specified functions
        There is a possibility of data loss, if the object is forced to convert to a particular data type

    Implicit Type Conversion in Python
        Here, the Python interpreter automatically converts one data type to another without any user involvement

    Explicit Type Conversion in Python
        Here, the data type is manually changed by the user as per their requirement
        Also, there is a risk of data loss since we are forcing an expression to be changed in some specific data type

    Various forms of explicit type conversion:
        Converting integer to float
            int(a): This function converts any data type to an integer.
            float(): This function is used to convert any data type to a floating-point number.
'''

x = 10      # implicit conversion
y = 10.6    # implicit conversion
z = x + y   # implicit conversion

print ("x is of type, ", type(x))
print ("y is of type, ", type(y))
print ("z is of type, ", type(z))

str = "10"    # initializing string
num = int(str)  # explicit type conversion
floatNum = float(str)

print(num)
print(type(num))

print(floatNum)
print(type(floatNum))

str1 = "10.6"
num1 = float(str1)  # explicit type conversion
print(type(num1))

int1 = 10
intToFloat = float(int1)
print(type(intToFloat))

float1 = 10.6
floatToInt = int(float1)
print(type(floatToInt))

s1 = "71,200"
s1 = s1.replace(',','')
print(type(s1))
print(type(int(s1)))