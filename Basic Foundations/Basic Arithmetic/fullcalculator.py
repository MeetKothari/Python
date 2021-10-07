def add(x,y):
    return float(x + y)

def subtract(x,y):
    return float(x - y)

def multiply(x,y):
    return float(x * y)

def divide(x,y):
    return float(x / y)

print('\nHello. Select the operation you would like to execute: ')
print('\n1. Add')
print('\n2. Subtract')
print('\n3. Multiply')
print('\n4. Divide')

while (True):

    operation = input('\nPlease enter your choice: ')
    
    if operation in ('1', '2', '3', '4'):
        
        num1 = float(input('\nEnter first number: '))
        num2 = float(input('Enter second number: '))

        if operation == '1': print(num1, '+', num2, '=', add(num1, num2))

        elif operation == '2': print(num1, '-', num2, '=', subtract(num1, num2))

        elif operation == '3': print(num1, '*', num2, '=', multiply(num1, num2))

        elif operation == '4': print(num1, '/', num2, '=', divide(num1, num2))
        
        next_calculation = input('\nDo you want to do another calculation? (y/n):')
        
        print('\n\n')
        
        if next_calculation == 'n': break
        if next_calculation == 'N': break

    else: print('Invalid Input')
