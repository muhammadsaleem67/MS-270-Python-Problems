def flatten_list(nested_lst):
    flat = []
    
    for item in nested_lst:
        # Check if the current item is a list itself
        if isinstance(item, list):
            # Recursively call flatten_list and extend our current flat list
            flat.extend(flatten_list(item))
        else:
            # If it's a normal element, just append it
            flat.append(item)
            
    return flat
print(flatten_list([1, [2, 3], [4, [5, 6]], 7]))
# Output: [1, 2, 3, 4, 5, 6, 7]
"""
	1. Type Checking: We iterate through the main list. We use isinstance(item, list) to ask Python: "Is this specific item a list?"
	2. Recursion (extend): If it is a list, we call flatten_list() on that sub-list. The .extend() method takes the results and unwraps them into our main flat list (unlike .append(), which would just drop the list in as a whole chunk).
	3. Base Case (append): If the item is just a regular number/string, we simply .append() it to our flat list.
"""