myDict = dict()
print(myDict)
myDict = {'name': 'Alex', 'Age': 35}
print(myDict)
myDict = dict(Name='Alex', Age=30, isMale=True)
print(myDict)
print(myDict['Age'])

print('----------------')
for key in myDict:
    print(key, '=', myDict[key])
myTuple = ('Name', 'Age', 'isMale')
for a in myTuple:
    print(a, '=', myDict[a])

print('----------------')
myDict = {str(i * 2): i for i in range(1, 10)}
print(myDict)

print('------------')
myDict = dict(Name='No name', age=0)
print(myDict)
print('Enter name')
a = input()
print('Enter age')
b = input()
myDict = dict(name=a, age=b)
for key in myDict:
    print(key, '=', myDict[key])
