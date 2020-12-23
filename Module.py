def minfunc(arr):
    min = arr[0]
    for a in arr:
        if min > a:
            min = a
    return min

def maxfunc(arr):
    max = arr[0]
    for a in arr:
        if max < a:
            max = a
    return max

def avfunc(arr):
    a = 0
    for b in arr:
        a += b
    return a / len(arr)