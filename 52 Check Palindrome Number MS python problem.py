def ispallingdrome(num):
    # convert to string and compare it to its reverse
    num_str = str(num)
    return num_str == num_str[::-1]
print(ispallingdrome(12321))
print(ispallingdrome(3423))

"""
	1. String Conversion: The easiest way to reverse a sequence in Python is to treat it as a string. We convert num to num_str.
	2. Slicing: num_str[::-1] is Python shorthand for "create a copy of this string, stepping backward by 1 character at a time."
	3. Comparison: We check if the original string is exactly equal to the reversed string and return True or False.
"""