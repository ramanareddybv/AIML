#firstName = input("Enter your firstName: ")
#lastName = input("Enter your lastName: ")

#print("Your fullName is: " + firstName + ' ' + lastName)
#print("Your fullName is: ", firstName, lastName)

#name, hobby = input("Enter your name and hobby separated by whitespace: ").split()
#print(name, 'likes', hobby)

#name1, hobby1 = input("Enter your name and hobby separated by ,: ").split(',')
#print(name1, 'likes', hobby1)

#int1 = int(input("Enter 1st number: "))
#int2 = int(input("Enter 2nd number: "))
#print('SUM = ', int1+int2)

#float1 = float(input("Enter 1st number: "))
#float2 = float(input("Enter 2nd number: "))
#print('SUM = ', float1+float2)

# map() syntax map(function, sequence)
n1, n2, n3 = map(float, input("Enter three float numbers: ").split())
print('SUM = ', n1+n2+n3)

mylist = [23, 25, 5, 26]
convertToFloat = map(float, mylist)
a, b, c, d = map(float, mylist)
print(convertToFloat)
print(a,b,c,d)