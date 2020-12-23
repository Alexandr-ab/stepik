i = 0
while i < 10:
    print('Hello World!')
    i += 1  # i = i + 1
print('Cycle ends')
print('-----------')

i = 0
while i < 10:
    i += 1
    print(i)

print('-----------')

i = 0
while i < 10:
    i += 1
    if i != 5:
        print(i)

print('-----------')

i = 0
while i < 10:
    i += 1
    if i == 5:
        continue
    if i == 8:
        break
    print(i)

print('----------')

s = 0
x = 1
to = 10
while x <= to:
    s += x
    x += 1
print(s)

print('-----------------')

# while True:
#     code = input('0 for exit: ')
#     if code == '0':
#         break

print('------------')

# exit(0)
#
#
# i = 0
# while True:
#     i += 1
#     print(i)

x = 0

while True:
    a = input('Enter number: ')
    if a == 'sum':
        print(x)
        x = 0
        continue
    if a == 'exit':
        break
    x = x + int(a)
