arr = []
print(arr)
arr = ['H', 'e', 'l', 'l', 'o']
print(arr)

print(arr[1])

print('Last element:', arr[-1])     # First from the end
print('Last element:', arr[-2])     # Second from the end
print('Length of arr :', len(arr))
print('last element:', arr[len(arr) - 1])

print('-----------')

i = 0
while i < len(arr):
    print(arr[i])
    i += 1

print('--------------')

arr = ['a', 3, 5.8, True]
i = 0
while i < len(arr):
    print(arr[i])
    i += 1

arr[1] = 'b'
print(arr)

# arr[4] = 9   # Error

arr[len(arr) - 1] = False
print(arr[len(arr) - 1])

print('---------------')

arr = [[2, 3], [4, 5, 6]]
print(arr[0])
print(arr[1])
print(arr[0][1])

i = 0
while i < len(arr):
    j = 0
    while j < len(arr[i]):
        print(arr[i][j])
        j += 1
    i += 1
print('---------------')

arr = [20, 30, 15, 45, 15]
mini = arr[0]
maxi = arr[0]
i = 1
while i < len(arr):
    if arr[i] < mini:
        mini = arr[i]
    if arr[i] > maxi:
        maxi = arr[i]
    i += 1
print(arr)
print(mini)
print(maxi)
print('----------------------')

arr = ['a', 'b', 'c', 'd', 'e', 'f']
i = 0
while i < len(arr):
    print(i, '-', arr[i])
    i += 1

while True:
    print('enter index:')
    a = input()
    if int(a) >= len(arr):
        print('Wrong number')
    else:
        print(arr[int(a)])
        break
