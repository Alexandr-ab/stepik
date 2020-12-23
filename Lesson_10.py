arr = [1, 5, 0, -5, 2.5]
for n in arr:
    print(n)
print('-------------')

string = 'Python'
print(string[0])

for s in string:
    print(s)
print('-------------')
for s in string:
    print(s)
    if s == 'y':
        break
else:
    print('Symbol y in', string, 'doesn\'t exist')
print('-------------')
arr = list(range(2, 15))
print(arr)
for n in arr:
    print(n)
print('--------')
arr = [i for i in range(1, 10)]
print(arr)
arr = [i * 2 for i in range(1, 10)]
print(arr)
arr = [i for i in range(1, 10) if i % 2 == 0]
print(arr)

print('------------')

arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
i = 0
n = 0
while n < 9:
    i += 2
    arr[n] = i
    n += 1

print(arr)
print('----------')

arr = [1, 6, 34, 2, 9]
x = 0
for n in arr:
    x = x + n
print(x)
print('-------------')
x = 0
for n in arr:
    x = x + n
x = x / len(arr)
print(x)
