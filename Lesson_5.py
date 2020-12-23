a = True
b = False
print('a =', a)
print('b =', b)

print('a or b =', a or b)
print('a and b =', a and b)
print('not a =', not a)
print('a != b =', a != b)
print('a == b =', a == b)

print('-------------------')

x = 5
y = 7
print('x =', x)
print('y =', y)

print('x > y =', x > y)
print('x < y =', x < y)
print('x <= y =', x <= y)
print('x >= y =', x >= y)
print('7 < 7 =', 7 < 7)
print('7 <= 7 =', 7 <= 7)

print('x and a or (x > 10) =', x and a or (x > 10))

print(True and (True or (False and True or False) and True or True != False))
print(15 > 20 or (5 < 7 and 8 > 12 or 12 >= 12 and 15 < 18))
