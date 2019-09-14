def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        less = [i for i in arr[:len(arr) // 2] + arr[(len(arr) // 2 + 1):] if i <= pivot]
        greater = [i for i in arr[:len(arr) // 2] + arr[(len(arr) // 2 + 1):] if i > pivot]

        return quick_sort(less) + [pivot] + quick_sort(greater)

lst = [2, 5, 8, 1, 4, 6, 78]
print(quick_sort(lst))