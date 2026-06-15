numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# Use filter to keep only the numbers that are even
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
# Output: [2, 4, 6, 8]
"""
	1. The filter() Function: filter() also takes two arguments: a function that returns True or False, and a list of data.
	2. The Condition: We use a lambda function lambda x: x % 2 == 0. This checks if a number divides cleanly by 2.
	3. Execution: filter() passes every number from the list into the lambda. If the lambda evaluates to True, filter() keeps the number. If it evaluates to False, filter() throws the number away.
	4. The list() Conversion: Just like map(), filter() returns a memory-efficient iterator object, so we wrap it in list() to get our final bracketed array.
"""