result = 0

def sum(x, y):
    s = float(x) + float(y)
    return s

def sub(x, y):
    global result
    result = float(x) - float(y)


x = input('Num 1:')
y = input('Num 2:')

print('Summary =', sum(x, y))
sub(x, y)
print('sub =', result)

print('------------')

pi = 3.141592

def round(x):
    r = pi * x * x
    return r

print(round(6))