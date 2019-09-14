def selection_sort(arr):
    min_el, min_in = 0, 0
    for i in range(len(arr) - 1):
        min_el = arr[i]
        for j in range(i, len(arr)):
            if arr[j] < min_el:
                min_el = arr[j]
                min_in = j
        arr[i], arr[min_in] = arr[min_in], arr[i]
        print(arr)
    return arr

lst = [2, 46, 10, 7, -45, 23, 44, 789, -89, 16, 0]
print(selection_sort(lst))