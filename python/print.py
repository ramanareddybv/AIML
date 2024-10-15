# print with single, double and triple quotes
print("----------print with single, double and triple quotes Syntax----------")
print('Hi Ram - How are you?')
print("Hi Ram - How are you?")
print('''Hi Ram - How are you?
I am doing good
Thank you!''')
print("""Hi Ram - How are you?
I am doing good
Thank you!""")
print("Happy 'Diwali' Ram!")
print('Happy "Diwali" Ram!')

# escape sequence \n \t \
print("----------Escape Sequence Syntax----------")
print("Happy \"Diwali\" Ram!")
print("Ram Shilpa Seetha")
print("Ram\tShilpa\tSeetha")
print("Ram\nShilpa\nSeetha")
print("Ram\nShilpa\tSeetha")
print("c:\newFolder\newFiles\newfile.txt")
print("c:\\newFolder\\newFiles\\newfile.txt")

# Raw String
print("----------Raw String Syntax----------")
print(r"c:\newFolder\newFiles\newfile.txt")
print(R"c:\newFolder\newFiles\newfile.txt")
filePath1 = r"c:\newFolder\newFiles\newfile.txt"
filePath2 = R"c:\newFolder\newFiles\newfile.txt"
print(filePath1)
print(filePath2)

# Variables printing
a = 20
b = "Hi Ram"
print(a, b)
print(10, "Hi Ram")

print("Hi Ram, Your are in " + str(42) + " age")

name = "Ram"
code = 'D1006'
doj = '07-01-2020'
exp = 18

# long format
mymsg = "My name is {}, My code is {} and I have {} years of exp"
print(mymsg.format(name, code, exp))

# short format
print(f"My name is {name}, My code is {code} and I have {exp} years of exp")
