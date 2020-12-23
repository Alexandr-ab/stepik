myTuple = tuple()
print(myTuple)
myTuple = (1, '3', '5')
print(myTuple)

myTuple = (1,)  # 1 elem tuple
print(myTuple)

myTuple = tuple('Python')
print(myTuple)
print('------------')

print('Enter string')
a = input()

myTuple = tuple(a)

for n in myTuple:
    print(n)
