def sort_string(text):
    # sorted() turns the string into an alphabetically sorted list of characters
    sorted_list = sorted(text)
    
    # Join the list back into a string
    return "".join(sorted_list)
print(sort_string("python")) # Output: hnopty
"""
	1. The sorted() Function: When you pass a string into sorted(), Python breaks it apart, sorts the characters by their ASCII values (alphabetically), and returns a list (e.g., ['h', 'n', 'o', 'p', 't', 'y']).
	2. Rejoining: Because we want a string as our final output, not a list, we use "".join() to fuse the characters back together.
"""