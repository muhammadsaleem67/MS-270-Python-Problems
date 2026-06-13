def binary_to_decimal(binary_str):
    decimal = 0
    # reversed the string to start from the lowest power of 2 
    reversed_bin = str(binary_str)[::-1]
    for i in range(len(reversed_bin)):
        bit = int(reversed_bin[i])
        # multiply the bit (0 or 1) by 2 raised to the power of its position 
        decimal += bit * ( 2 ** i)

    return decimal
print(binary_to_decimal("11001")) 
"""
	1. Reversing: We reverse the binary string using Python's slicing trick [::-1]. This makes it easier to process because the first character in our reversed string now correctly represents $2^0$, the second represents $2^1$, and so on.
	2. The Loop: We loop through each character using its index (i).
	3. The Math: We convert the character back to an integer (a 0 or a 1). Then, we multiply that bit by $2^i$. If the bit is 1, it adds that power of 2 to our decimal total; if it's 0, it adds nothing.
"""