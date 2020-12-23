import random

mySet = set()
print(mySet)
mySet = {}
print(mySet)

mySet = set('PythononPyt')
print(mySet)

mySet = {1, 'y', 2, 1, '1'}
print(mySet)
print('-------------')

print(int(random.random() * 10))
arr = [int(random.random() * 10) for i in range(0, 10)]
print(arr)
mySet = set(arr)
print(mySet)
print('-----------------')
arr = [int(random.random() * 10) for i in range(0, 10)]
print(arr)
arr = list(set(arr))
print(arr)
print('-------------')

print('Enter length of array')
a = int(input())
arr = [int(random.random() * 100) for i in range(0, a)]

n = 0
while n < a:
    print(arr[n])
    n += 1

arr = set(arr)
print('==========')
for s in arr:
    print(s)
