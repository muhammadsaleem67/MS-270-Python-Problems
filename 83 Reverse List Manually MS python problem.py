def reverse_list(lst):
    left = 0
    right = len(lst) - 1
    
    # Keep swapping until the pointers meet in the middle
    while left < right:
        # Swap the elements
        lst[left], lst[right] = lst[right], lst[left]
        
        # Move pointers inward
        left += 1
        right -= 1
        
    return lst
print(reverse_list([1, 2, 3, 4, 5])) # Output: [5, 4, 3, 2, 1]
"""
	1. Two Pointers: We set a left pointer to the start of the list (index 0) and a right pointer to the end (index len(lst) - 1).
	2. The Loop: A while loop runs as long as left is strictly less than right.
	3. The Swap: Python allows simultaneous assignment. lst[left], lst[right] = lst[right], lst[left] perfectly swaps the elements at the two indices.
	4. Closing In: We increment left by 1 and decrement right by 1, moving both pointers one step closer to the center before repeating.
"""