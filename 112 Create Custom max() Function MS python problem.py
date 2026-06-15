def custom_max(iterable):
    if not iterable:
        return None # Handle empty lists or strings
        
    # Assume the first item is the largest to start
    largest = iterable[0]
    
    # Iterate through the rest of the items
    for item in iterable[1:]:
        if item > largest:
            largest = item
            
    return largest
print(custom_max([10, 45, 2, 99, 30])) # Output: 99
