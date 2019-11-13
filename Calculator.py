x = float(input('First: '))
y = float(input('Second: '))
operation = (input('What do you want: '))

result = None
if operation == '+':
    result = x + y
elif operation == '-':
    result = x - y
elif operation == '/':
    result = x / y
elif operation == '*':
    result = x * y
else:
    print('Impossible operation')

if result is not None:
    print('Result', result)