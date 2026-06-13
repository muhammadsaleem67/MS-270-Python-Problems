def find_frequency(lst):
    freq = {}
    
    for item in lst:
        if item in freq:
            # If the item is already a key, increment its count
            freq[item] += 1
        else:
            # If we haven't seen it yet, add it to the dictionary with a count of 1
            freq[item] = 1
            
    return freq
print(find_frequency(["apple", "banana", "apple", "cherry", "banana", "apple"]))
# Output: {'apple': 3, 'banana': 2, 'cherry': 1}
"""
	1. The Dictionary: We initialize an empty dictionary freq to store our items as keys and their counts as values.
	2. The Loop & Check: We iterate through the list. For each item, we check if it already exists inside the dictionary.
	3. Updating: If it exists, we add 1 to its current value. If it does not exist, we create a new entry for it and set its value to 1.
"""