firstName = 'Ram'
lastName = 'Bhumireddy'
fullName = firstName + ' ' + lastName
print(fullName)

str = "Ram,Bhumireddy"
str = str.replace(',', '')
print(str)

# split the string and returns a List object and by default it takes white space as a seperator
str1 = "Ram Shilpa Seetha"
nameList = str1.split()
print(nameList)

name1, name2, name3 = str1.split()
print(name1, name2, name3)