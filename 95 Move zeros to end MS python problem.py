def move_zeros(list):
    insert_pos = 0
    # first pass: move all non-zero elements to the front
    for i in range(len(list)):
        if list[i] != 0:
            # Swap the non-zero element to the corrent insert position
            list[insert_pos], list[i] = list[i], list[insert_pos]
            insert_pos += 1
    return list
print(move_zeros([4,6,4,0,5,0,7,9,0,0,7,0,0,7,6,5,9]))

"""
	1. The Pointer: We create a variable called insert_pos starting at index 0. This pointer keeps track of where the next non-zero number belongs.
	2. The Swap: We iterate through the list. Whenever we find a number that is not a zero, we swap it with whatever is sitting at insert_pos.
	3. Progression: After a swap, we increment insert_pos by 1. Because we swap, all the zeros naturally get pushed backward until they hit the end of the list.
"""