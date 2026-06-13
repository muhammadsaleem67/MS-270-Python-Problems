def nth_fibonacci(num):
    if num<= 0:
        return "Invalid input"
    elif num == 1:
        return 0
    elif num == 2:
        return 1
    a, b = 0, 1
    # loop to step through the sequence 
    for i in range(2, num):
        a, b = b, a + b
    return b
print(nth_fibonacci(7)) 

"""
	1. Edge Cases: The 1st number is 0, the 2nd is 1. We handle these immediately.
	2. Tracking State: We initialize a to 0 and b to 1. These represent the "two previous numbers".
	3. Simultaneous Assignment: In the loop, a, b = b, a + b does two things at once: it slides a up to the current b value, and it calculates the new b by adding the old a and b together. This repeats until we reach the $n$-th spot.

"""
