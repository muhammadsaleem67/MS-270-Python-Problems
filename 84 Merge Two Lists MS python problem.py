def merge_lists(list1, list2):
    merged = []
    
    for item in list1:
        merged.append(item)
        
    for item in list2:
        merged.append(item)
        
    return merged
print(merge_lists([1, 2], [3, 4])) # Output: [1, 2, 3, 4]
"""
	1. Empty Vessel: We create an empty list called merged.
	2. Sequential Appending: We loop entirely through list1, appending every item to merged. Once that finishes, we loop through list2, appending its items to the end of merged.
"""