def factorial_iterative(n):
    if n < 0:
        return None # Factorials for negative numbers are undefined
        
    result = 1
    # Loop from 1 up to n
    for i in range(1, n + 1):
        result *= i
        
    return result
print(factorial_iterative(5)) # Output: 120 (5 * 4 * 3 * 2 * 1)
"""
	1. Base Total: We start with result = 1. (If we started with 0, multiplying anything by it would just remain 0).
	2. The Loop: We use range(1, n + 1) to generate every number from 1 up to our target number n.
	3. Multiplication: We continuously multiply our result by i during every loop iteration.
"""