def find_missing_number(arr):
    # The array is supposed to have 'n' numbers.
    # since one is missing, 'n' is the length of the array + 1
    n = len(arr)
    # Mathematical formula for the sum of the first n natural numbers: 
    expected_sum = n * (n + 1) // 2
    # the actual sum of the numbers in our array
    actual_sum = sum(arr)
    # difference is exactly our missing number
    return expected_sum - actual_sum
sequence = [0, 1, 2, 3, 4, 5]
print(find_missing_number(sequence))
"""
	1. Finding N: If the sequence has a missing number, the highest number $n$ should be equal to len(arr) (because the sequence includes 0).
	2. The Formula: Gauss's formula for the sum of consecutive integers from $0$ to $n$ is $\frac{n(n + 1)}{2}$. We use floor division // to keep it an integer. This gives us what the sum should be if nothing was missing.
	3. Subtraction: We add up the actual numbers in the array using sum(arr). Subtracting the actual sum from the expected sum gives us the exact value of the missing number.
"""