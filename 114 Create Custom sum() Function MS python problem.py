def custom_sum(iterable, start=0):
    total = start
    for item in iterable:
        total += item
    return total
print(custom_sum([10, 20, 30]))       # Output: 60
print(custom_sum([10, 20, 30], 100))  # Output: 160 (Starts counting from 100)
"""
	1. The Default Parameter: We add start=0 as a default argument. This means if the user just passes a list, we start counting from 0. If they pass a second number, we start our total at that number.
	2. Accumulation: We iterate through every item in the list and continuously add it to our total variable.
"""