def binary_search(sorted_list, guess):
    low = 0
    high = len(sorted_list) - 1
    while low <= high:
        mid = (high + low) // 2
        if sorted_list[mid] == guess:
            return mid
        elif sorted_list[mid] < guess:
            low = mid + 1
        else:
            high = mid - 1
    return None

lst = [1, 78, 45, 6, 123, 2, 10, 7, 98, 46, 55, 32, 77]
lst.sort()
print(lst)
print(binary_search(lst, 24))
print(binary_search(lst, 77))