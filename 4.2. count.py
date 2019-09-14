def count(arr):
    if arr == []:
        return 0
    else:
        return 1 + count(arr[1:])

lst = [2, 5, 8, 1, 48]
print(count(lst))