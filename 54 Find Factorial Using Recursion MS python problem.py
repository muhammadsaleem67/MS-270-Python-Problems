def factorial(num):
    # bases
    if num < 0 :
        return None
    elif num == 0 or num == 1:
        return 1
    # recursive cases num* (num - 1)!
    return num * factorial(num-1)
print(factorial(5))

"""
	1. The Base Case: Every recursive function needs a stopping point so it doesn't loop infinitely. By definition, $0!$ and $1!$ both equal 1. When n hits 1 or 0, we return 1.
	2. The Recursive Call: We return n multiplied by the result of calling the exact same function again, but passing it n - 1. For 5, it returns 5 * factorial_recursive(4). This chains down until it hits the base case, then bubbles the math back up to give the final answer.
"""