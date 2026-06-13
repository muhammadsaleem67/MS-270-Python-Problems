def find_gcd(a, b):
    # Euclidean algorithm
    while b!= 0:
        a, b = b, a % b
    return a
print(find_gcd(48, 18))
num1 = int(input("Number 1 : "))
num2 = int(input("Number 2 : "))
print(find_gcd(num1, num2))
"""
	1. The Euclidean Algorithm: This mathematical principle states that the GCD of two numbers also divides their difference. In programming, we use remainders to do this quickly.
	2. The while loop: As long as b is not 0, we perform a simultaneous swap. a gets the value of b, and b gets the remainder of a / b.
	3. Result: When b finally hits 0, a holds the Greatest Common Divisor.

"""