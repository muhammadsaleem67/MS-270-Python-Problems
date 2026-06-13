def find_common(list1, list2):
    # Convert lists to sets and use the intersection operator (&)
    common_elements = set(list1) & set(list2)
    return list(common_elements)
print(find_common([1, 2, 3, 4], [3, 4, 5, 6])) # Output: [3, 4]
"""
	1. Set Conversion: We convert both lists into sets. Sets are mathematical objects in Python designed specifically for these types of operations.
	2. Intersection: The & operator, when used between two sets, automatically returns a new set containing only the elements present in both.
	3. Back to List: We wrap the result in list() to return the data structure requested by the prompt.
"""