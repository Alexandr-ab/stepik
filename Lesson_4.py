x = 7
y = 3
print('x =', x)
print('y =', y)

# Base math
print('x + y =', x + y)
print('x - y =', x - y)
print('x * y =', x * y)
print('x / y =', x / y)
print('x % y =', x % y)     # Остаток от деления
print('x // y =', x // y)     # Целое от деления
print('x ** y =', x ** y)     # возведение в степень

# битовые операции
x = 5
y = 7
print('x =', x, '=', bin(x))
print('y =', y, '=', bin(y))
print('20 =', hex(20))
print('20 =', oct(20))
print('------------')
print('x | y =', x | y)     # или
print('x | y =', bin(x | y))     # или
print('x & y =', x & y)     # и
print('x & y =', bin(x & y))     # и
print('x ^ y =', x ^ y)     # исключающее или
print('x ^ y =', bin(x ^ y))     # исключающее или
print('~x =', ~x)     # битовое отрицание
print('~x =', bin(~x))     # битовое отрицание
print('x << 1 =', x << 1)   # сдвиг на 1 бит влево
print('x << 1 =', bin(x << 1))   # сдвиг на 1 бит влево
print('x >> 1 =', x >> 1)   # сдвиг на 1 бит вправо
print('x >> 1 =', bin(x >> 1))   # сдвиг на 1 бит вправо

a = int(((15 * 10 - 20) / 2) + 14 * 10 + (-45))
print(a)
a = bin(a)
print(a)
