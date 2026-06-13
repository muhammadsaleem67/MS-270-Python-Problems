def list_intersection(list1, list2):
    # Use a list comprehension for a clean, one-line loop
    return [item for item in list1 if item in list2]
print(list_intersection(["apple", "banana", "cherry"], ["banana", "date"])) 
# Output: ['banana']
