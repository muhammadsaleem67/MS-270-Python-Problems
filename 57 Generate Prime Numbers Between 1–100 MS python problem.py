def generate_primes(limit):
    primes = []
    for num in range(2, limit + 1):
        # we only need to check divisiblity up to the square root of the number
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break # Not prime, exit the inner loop early
        if is_prime:
            primes.append(num)
    return primes
print(generate_primes(100))
"""
	1. Outer Loop: We iterate through all numbers from 2 up to the limit (100).
	2. Inner Loop (Efficiency): To check if num is prime, we don't need to check all numbers up to num. We only need to check up to its square root (int(num 0.5) + 1). If a number has a factor larger than its square root, it must also have a factor smaller than it.
	3. The Flag & Break: We assume the number is prime (is_prime = True). If we find any number that divides evenly (num % i == 0), we flag it as False and immediately break out of the inner loop to save processing time.
"""