def reverse_dictionary(d):
    # use a dictionary comprehension to flip item
    return {value : key for key, value in d.items()}
original = {"apple":"red", "banana":"yellow", "lime":"green"}
print(reverse_dictionary(original))
# Output: {'red': 'apple', 'yellow': 'banana', 'green': 'lime'}
