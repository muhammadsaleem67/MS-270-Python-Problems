def reverse_binary(num):
    # bin() returns a string like '0b1101', so we slice [2:] to remove the '0b'
    binary_str = bin(num)[2:]
    reversed_bin = binary_str[::-1]
    # convert back to an integer from base-2
    return int(reversed_bin, 2)
print(reverse_binary(13)) # 13 is 1101 in binary. Reversed is 1101, which is 11
"""
	1. Binary Conversion: Python's bin() function converts numbers to binary, but prepends 0b. We use slicing [2:] to chop off the first two characters.
	2. Reversing: We use string slicing [::-1] to flip the binary digits.
	3. Back to Decimal: The int(string, base) function takes our reversed binary string and reads it as a base-2 number, outputting the standard integer value.
"""