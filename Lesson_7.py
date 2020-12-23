print('Enter 1, 2 or 3: ')
a = input()
if a == '1':
    print('Entered one')
    print('it\'s lower than 10')
    if 5 == 5:
        print('yahoo!')
elif a == '2':
    print('Entered two')
elif a == '3':
    print('Entered three')
else:
    print('Entered wrong number')

cond = a == '0' or a == '1' or a == '3'

if cond:
    x = 1
else:
    x = 0

print(x)

x = 'xTrue' if cond else 'xFalse'
print(x)
print('---------------')

print('enter number 1:')
num1 = input()
print('enter number 2:')
num2 = input()
if num2 == '0':
    a = 'Endless'
    print(num1, '/', num2, '=', a)
else:
    a = int(num1) / int(num2)
    print(num1, '/', num2, '=', int(a))
