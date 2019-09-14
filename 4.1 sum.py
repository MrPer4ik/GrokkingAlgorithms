def sum(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + sum(arr[1: len(arr)])

lst = [2, 5, 8, 1]
print(sum(lst))