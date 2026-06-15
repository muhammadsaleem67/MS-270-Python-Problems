numbers = [1, 2, 3, 4, 5]
# Use map to apply a lambda function (doubling) to every item in the list
doubled_numbers = list(map(lambda x: x * 2, numbers))
print(doubled_numbers)
# Output: [2, 4, 6, 8, 10]
"""
	1. The map() Function: map() takes two arguments: a function, and a list of data.
	2. The Lambda: Instead of writing a separate function to double numbers, we create a lambda function (lambda x: x * 2) right inside the map() call.
	3. Execution: map() takes the first number (1), passes it to x, doubles it, and holds onto the 2. Then it grabs the next number (2), doubles it, and so on.
	4. The list() Conversion: In Python 3, map() returns a "map object" (an iterator) to save memory. To see the actual array of numbers, we must wrap it in list() to convert it back into a standard Python list.

"""