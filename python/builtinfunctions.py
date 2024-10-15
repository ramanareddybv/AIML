'''
    round function takes the floating point number and gives us the
    required numbers after decimal point based on the round
    number that we pass to the function and increase the value to 1
'''

floatNum = 566699.62958444
print(round(floatNum, 2))

var = 65544.34625
print(f"Short value is {var:.2f}")

complex = 27+47j
print(complex.real)
print(complex.imag)

a, b, c = 10, 20, 40
maxNum = max(a,b,c)
minNum = min(a,b,c)
print(maxNum)
print(minNum)