def find_pair(list, target):
    # use a set to keep target
    seen = set() 
    for num in list:
        # Calculate what number we need to hit the target
        complement = target - num
        # check if we've already seen that needed number
        if complement in seen:
            return (complement, num)
        # add the current number to our set for future checks 
        seen.add(num)

    return None  
print(find_pair([2,7,11,15], 9))
"""
	1. The Setup: We create an empty set called seen. Sets have exceptionally fast lookups in Python.
	2. The Logic: As we loop through the list, we look at num and calculate its complement (i.e., target - num). If target is 9 and we are looking at 2, the complement we need is 7.
	3. The Check: We ask if 7 is already in our seen set. If it is, we've found our pair! If not, we add 2 to the set and move to the next number.
"""