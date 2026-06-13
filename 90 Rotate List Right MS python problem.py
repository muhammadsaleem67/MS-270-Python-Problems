def rotate_right(lst, positions):
    if not lst:
        return []
        
    n = positions % len(lst)
    
    # Slice the last 'n' elements, then add the rest
    return lst[-n:] + lst[:-n]
print(rotate_right([1, 2, 3, 4, 5], 2)) # Output: [4, 5, 1, 2, 3]
