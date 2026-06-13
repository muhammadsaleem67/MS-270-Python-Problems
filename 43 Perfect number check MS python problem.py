def is_perfect_number(num):
    if num <= 0:
        return False
        
    divisors_sum = 0
    # A number's proper divisors will never exceed half its value
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            divisors_sum += i
            
    return divisors_sum == num
print(is_perfect_number(28)) # Output: True (1+2+4+7+14=28)

divisorsum = 0
for i in range(10000):
    for j in range(1, i // 2 + 1):
        if i % j == 0 :
            divisorsum += j
            print(j)

"""
	1. Edge Case: Perfect numbers are positive integers, so anything 0 or below is immediately False.
	2. The Loop: We loop from 1 up to num // 2. We stop at half the number because no proper divisor can be larger than half of the number itself (e.g., you can't divide 28 by anything between 15 and 27 and get a whole number).
	3. Finding Divisors: The modulo operator (num % i == 0) checks if i divides evenly into num. If it does, we add it to our running total.

"""