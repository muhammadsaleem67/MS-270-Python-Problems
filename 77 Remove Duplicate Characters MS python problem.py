def remove_duplicates(text):
    # dict.fromkeys() creates a dictionary with characters as keys.
    # Dictionaries cannot have duplicate keys, and in modern Python, they keep order!
    unique_chars = dict.fromkeys(text)
    
    # Join the keys back into a single string
    return "".join(unique_chars)
print(remove_duplicates("programming")) # Output: progamin
