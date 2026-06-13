def calculate_power(base, exponent):
    if exponent == 0:
        return 1
    result = 1
    # loop 'exponent' number of times
    for i in range(abs(exponent)):
        result *= base

    # handling negative exponents (fractions)
    if exponent < 0:
        return 1 / result
    return result
print(calculate_power(2, 3))
print(calculate_power(2, -2))
"""
	1. Base Case: Anything to the power of 0 is 1.
	2. Iterative Multiplication: We loop exactly abs(exponent) times. In Python, using _ as a loop variable means "I just need the loop to run this many times; I don't need to use the number itself." We multiply result by the base each time.
	3. Negative Exponents: If the original exponent was negative, mathematical rules state that $x^{-y} = \frac{1}{x^y}$. We apply this rule before returning.
"""