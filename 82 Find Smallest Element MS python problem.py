def find_smallest(list):
    if not list: # Check if list is empty
        return None
        
    # Assume the first item is the smallest to start
    smallest = list[0]
    
    for num in list:
        if num < smallest:
            smallest = num
            
    return smallest
print(find_smallest([34, 15, 88, 2])) # Output: 2
"""
	1. The Baseline: We initialize our smallest variable using the very first element of the list (lst[0]).
	2. The Loop: We iterate through every number in the list.
	3. The Comparison: If the current num is strictly less than our recorded smallest, we overwrite smallest with this new, lower value.
"""