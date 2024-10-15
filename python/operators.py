'''
    Operators in Python
        - Assignment operator: =
        - Comparision operator: ==
        - Arithmetic: +, -, , /, *, //, %
        - Relational: >, <, >=, <=, !=
        - Logical: and, or, not
        - Unary:
            If the operator acts on a single operand then it's called the unary operator
            For example: in '-5' the operator '-' is unary operator
        - Ternary:
            The ternary operator in Python is a concise way of writing simple if/else statements in a single line
        - Membership: in, not in
        - Identity operator: is, is not

    Operator precedence
        THE EXECUTION OF EXPRESSION WILL BE FROM RIGHT TO LEFT BY DEFAULT

        Operator precedence - PEMDAS which means
            Parenthesis ()
            Exponential ** (power of)
            Multiplication *
            Division /
            Addition +
            Subtraction -
'''

# in, not in checks value but is, is not checks address of the variable (id)
print('I' in 'India')
print('i' in 'India')
print('k' in 'India')
print('na' in 'India')
print('na' not in 'India')
print('nd' in 'India')
print('Ind' in ['Japan', 'Chaina', 'Boston', 'India'])
print('Ind' not in ['Japan', 'Chaina', 'Boston', 'India'])
print('Ind' in ['Japan', 'Chaina', 'Ind', 'Boston', 'India'])
print(10 in [20, 20.5, 10, 3])

a = 30
b = 20
c = 30

print(a is b)
print(a is c)
print(a is not c)