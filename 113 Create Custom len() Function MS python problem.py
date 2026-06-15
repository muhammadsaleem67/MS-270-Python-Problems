def custom_len(iterable):
    count = 0
    # Loop through every item, ignoring what the item actually is
    for i in iterable:
        count += 1
    return count
print(custom_len("Python"))          # Output: 6
print(custom_len([1, 2, 3, 4, 5]))   # Output: 5
"""
	1. The Counter: We initialize a count variable at 0.
	2. The Loop: We loop over the iterable. We use an underscore _ because we don't actually care what the items are (we don't care if it's the letter 'P' or the number 3), we only care that they exist.
	3. Incrementing: For every item the loop encounters, we add 1 to our count.
"""