# import random
# import math as m
from random import *
from math import sin, cos
import math, cmath as cm
from calc import *
from Module import *

# print(random.randint(0, 10))
# print(m.sin(30))
print(randint(0, 10))
print(sin(1))
print(cos(1))
print(math.ceil(10.3))
print(cm.log10(1000))

while True:
    print('1 - sum, 2 - sub, 3 - mult, 4 - div, 0 - exit')
    code = input('Enter Command: ')
    if code == '0':
        break
    a = float(input('Num1: '))
    b = float(input('Num2: '))
    if code == '1':
        r = sum(a, b)
    elif code == '2':
        r = sub(a, b)
    elif code == '3':
        r = mult(a, b)
    elif code == '4':
        r = div(a, b)
    else:
        print('Wrong command')
        continue
    print('Result: ', r)

print('--------------')

print(minfunc([1, 4, 45, 32, -5, -23, 0]))
print(maxfunc([1, 4, 45, 32, -5, -23, 0]))
print(avfunc([1, 4, 45, 32, -5, -23, 0]))
