def binary_search(list, target):
    left = 0
    right = len(list) - 1
    while left <= right:
        # find the middle index
        mid = (left + right) // 2
        # check if target is exactly at the middle 
        if list[mid] == target:
            return mid
        # if target is greater, ignore the left half
        elif list[mid] < target:
            left = mid + 1
        # if target is smaller, ignore the right half 
        else :
            right = mid - 1
    # target is not present in array
    return -1
sorted_list = [2, 3, 4, 10, 40]
print(binary_search(sorted_list, 10))