num  = int(input("Enter the number to compare: "))
if num > 0:
    print(f"{num} is a positive number")
else:
    print(f"{num} is a negative number")

print("I am done!")


# True(all non zero values are True) / False (zero)
num = 5
if num:
    print(f'{num} is a number')

num1 = 0
if num1:
    print(f'{num} is a number')
else:
    print("number is zero")

num2 = 10
if type(num2) == int:
    print(f"{num2} is integer")

if isinstance(num2, int):
    print(f"{num2} is integer")

# one line statemt
x, y = 100, 200
print(f'{x} > {y}')     if (x > y)    else   print(f'{x} < {y}')

x, y = 100, 200
print(f'{x} > {y}') ; print("Hi Ram") ; print(x)    if (x > y)    else   print(f'{x} < {y}') ; print(y)

salary = 6000
bonus = salary * (50/100) if salary > 5000 else salary * (25/100)
print(f'bonus is {bonus}')

a, b, c = 12, 34, 8
if a > b and a > c:
    print('a ig big')
elif b > c:
    print('b is big')
else:
    print('c is big')

sex = input('Enter male/female [m/f]: ')
maritalStatus = input('Enter marital status [m/u]: ')
age = int(input('Enter age: '))

if maritalStatus == 'm':
    print('Driver is insured')
elif (sex == 'm' and age > 30) or (sex == 'f' and age > 25):
    print('Driver is insured')
else:
    print('Driver is not insured')


ms, gender, age = input("Enter ms[m/u], gender[m/f], age: ").split()
age = int(age)

if (ms == 'm') or (gender == 'm' and age > 30) or (gender == 'f' and age > 25):
    print('Driver is insured')
else:
    print('driver is not insured')