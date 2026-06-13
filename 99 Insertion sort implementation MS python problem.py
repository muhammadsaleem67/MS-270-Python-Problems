def insertion_sort(list):
    # start from the second element
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        # move elements that are greater than the key one position to the right
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j -= 1
        # Insert the key into its correct location
        list[j + 1] = key
    return list 
print(insertion_sort([57,53,23,67,43,75]))