
n1 = int(input('Please enter first number: '))
n2 = int(input('Please enter second number: '))
operator = input('Please enter operator [+] or [-] or [*] or [/]: ')
result = 0
if operator == '+':
    result = n1 + n2
    if result % 2 == 0:
        print(f'{n1} + {n2} = {result} - even')
    else:
        print(f'{n1} + {n2} = {result} - odd')
elif operator == '-':
    result = n1 - n2
    if result % 2 == 0:
        print(f'{n1} - {n2} = {result} - even')
    else:
        print(f'{n1} - {n2} = {result} - odd')
elif operator == '*':
    result = n1 * n2
    if result % 2 == 0:
        print(f'{n1} * {n2} = {result} - even')
    else:
        print(f'{n1} * {n2} = {result} - odd')
elif operator == '/':
    if n2 != 0:
        result = n1 / n2
        print(f'{n1} / {n2} = {result:.2f}')
    elif n2 == 0:
        print(f'Cannot divide {n1} by zero')

elif operator =='%':
    if n2 != 0:
        result = n1 % n2
        print(f'{n1} % {n2} = {result}')
    elif n2 == 0:
        print(f'Cannot divide {n1} by zero')
