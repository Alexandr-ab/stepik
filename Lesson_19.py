# a = 0
# while True:
#     a += 1
#     if a >= 25:
#         break
#     print('Hello')

arr = [1, -5, 43, -2, -6]
mas = [2, 54, -3, 54, -23]
def negative(arr):
    for n in arr:
        if n < 0:
            print(n)

negative(mas)