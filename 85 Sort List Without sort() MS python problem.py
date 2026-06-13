def bubble_sort(lst):
    n = len(lst)
    
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            
            # Swap if the element found is greater than the next element
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                
    return lst
print(bubble_sort([64, 34, 25, 12, 22, 11, 90])) 
# Output: [11, 12, 22, 25, 34, 64, 90]
"""
	1. Outer Loop: We loop n times to ensure we make enough passes over the list.
	2. Inner Loop: We loop from the beginning of the list up to n - i - 1. The - i is an optimization: after every full pass, the absolute largest number "bubbles" up to its correct spot at the very end, so we don't need to check those final slots again.
	3. The Swap: If the current item is larger than the item immediately to its right, they are out of order, so we swap them.
"""