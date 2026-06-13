def rotate_left(lst, positions):
    if not lst:
        return []
        
    # Prevent unnecessary full rotations
    n = positions % len(lst)
    
    # Slice from 'n' to the end, then add the beginning up to 'n'
    return lst[n:] + lst[:n]
print(rotate_left([1, 2, 3, 4, 5], 2)) # Output: [3, 4, 5, 1, 2]
"""
	1. Modulo Math: If a list is 5 items long, rotating it left 5 times results in the exact same list. We use modulo % len(lst) so if a user asks to rotate a 5-item list 12 times, the code mathematically reduces it to a much faster 2 rotations.
	2. List Slicing: Python's slicing [start:stop] is perfect here.
		○ lst[n:] grabs everything from index n to the end (the part that shifts to the front).
		○ lst[:n] grabs everything from the start up to index n (the part that wraps around to the back).
	3. Concatenation: We glue the two sliced lists together with +.
"""