def is_harshad(num):
    if num <= 0:
        return False
    # Sum the digits
    digit_sum = sum(int(digit) for digit in str(num))
    # Check if divisible
    return num % digit_sum == 0
print(is_harshad(18)) # Output: True
"""
	1. Summing Digits: We use our familiar string-conversion trick to add up the digits.
	2. Modulo Check: We use the modulo operator (%). If num % digit_sum equals 0, it means there is no remainder, proving it divides cleanly.

"""