def highest_value_key(d):
    if not d:
        return None        
    # Use max() and tell it to compare based on the dictionary's values
    return max(d, key=d.get)
scores = {"M Saleem": 85, "Babar A": 98, "Irfan A": 92}
print(highest_value_key(scores)) 
# Output: Babar A
"""
	1. The max() Function: Normally, calling max() on a dictionary just returns the highest key alphabetically (which would be "Charlie").
	2. The key Parameter: By passing key=d.get, we instruct the max() function to look up the value of each key and use those numbers to determine the winner. It then returns the original key that belonged to that winning number.
"""