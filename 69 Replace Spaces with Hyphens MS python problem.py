def first_non_repeating(text):
    # Dictionary to store character frequencies
    char_counts = {}
    
    # First pass: count all characters
    for char in text:
        char_counts[char] = char_counts.get(char, 0) + 1
        
    # Second pass: find the first one with a count of 1
    for char in text:
        if char_counts[char] == 1:
            return char
            
    return None # If all characters repeat

print(first_non_repeating("swiss")) # Output: w
"""
Frequency Map:** We use a dictionary to count how many times every letter appears. (e.g., `{'s': 3, 'w': 1, 'i': 1}`).
The Second Pass:** Because we want the *first* non-repeating character, we loop through the original text string a second time from left to right. We check our dictionary, and the very first character that has a count of exactly `1` is our winner.
"""