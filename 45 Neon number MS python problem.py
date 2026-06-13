def is_neon_number(num):
    square = num ** 2
    # Sum the digits of the squared number
    digit_sum = sum(int(digit) for digit in str(square))
    return digit_sum == num
print(is_neon_number(9)) # Output: True
for i in range(100000):
    square = i ** 2
    # Sum the digits of the squared number
    digit_sum = sum(int(digit) for digit in str(square))
    if i == digit_sum:
        print(i)


"""
	1. Squaring: We find the square of the number.
	2. Digit Summation: We convert the squared number to a string, iterate through each character, convert it back to an integer, and sum them up.
	3. Comparison: We check if the sum of the squared digits matches the original number.
"""
