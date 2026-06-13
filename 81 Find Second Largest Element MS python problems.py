def second_largest(list):
    if len(list) < 2:
        return None
        
    # Start with negative infinity
    largest = second = float('-inf')
    
    for num in list:
        if num > largest:
            # Shift the old largest down to second place
            second = largest
            largest = num
        elif num > second and num != largest:
            # Update second place if the number sits between second and largest
            second = num
            
    return second if second != float('-inf') else None
print(second_largest([10, 5, 20, 8, 20])) # Output: 10
"""
	1. Initialization: We create variables largest and second and set them to negative infinity. This ensures any real number in the list will be larger than our starting baseline.
	2. The Primary Check: If the current num is strictly greater than largest, we push our old largest value down into the second spot, and assign the new champion to largest.
	3. The Secondary Check: If the number isn't the absolute largest, but it is bigger than the current second, we update second. The num != largest check ensures we don't accidentally count duplicate maximums (like the two 20s in the example).
"""