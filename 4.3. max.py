def max(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        m = max(arr[1:])
        if arr[0] > m:
            return arr[0]
        else:
            return m

lst = [2, 5, 8, 1, 4, 6, 78]
print(max(lst))