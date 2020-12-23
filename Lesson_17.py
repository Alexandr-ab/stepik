try:
    a = float('abc')
except ValueError:
    print('Can\'t get number')

while True:
    a = input('Enter positive number: ')
    if a == 'exit':
        break
    try:
        a = float(a)
        if a <= 0:
            raise Exception('Negative')
    except ValueError:
        print('Can\'t get number')
    except Exception as exp:
        print(exp)
    else:
        print('thx for correct')
    finally:
        print('Exit anyway')
        break

print('-------------')


a = input('Num 1: ')
b = input('Num 2: ')
try:
    d = int(a) / int(b)
except ZeroDivisionError:
    print('Infinity')
else:
    print('Result is: ', d)
