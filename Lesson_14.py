def printpython():
    print('Enter smtg')
    inp = input()
    print(inp)


def summa(x, y):
    return x + y


s = summa(5, 8)

print(s)


def sub(x, y):
    return x - y


print(sub(34, 3))


def sumprint(x, y, r=False):
    a = summa(x, y)
    if r:
        return a
    else:
        print(a)


sumprint(6, 7, True)


print(sub(y=10, x=5))


def bigsum(*numbers):
    s = 0
    for n in numbers:
        s += n
    return s


print(bigsum(1, 5, 7, 3, 43))


def printdict(**dict):
    for key in dict:
        print(key, '=', dict[key])

printdict(name='Alex', age=30)

print('Anonymous functions')

lambdafunc = lambda x, y: print(x + y)
result = ((lambda x, y: x + y) (1, 3))
print(result)

def getmax(arr):
    max = arr[0]
    for n in arr:
        if n > max:
            max = n
    return max

print('------------------------------')
print(getmax([1, 5, 3, 56, 65, 23]))
print(getmax([1, 5, 3, 6, -65, 23]))

print('---------------')

def pare(x):
    if x % 2 == 0:
        a = True
    else:
        a = False
    return a
print(pare(3))

print('----------')

def avsum(*numbers):
    s = 0
    for n in numbers:
        s += n
    return s / len(numbers)

print(avsum(10, 20))