def find_duplicates(text):
    duplicates = []
    # Using a set to keep track of characters we've already seen
    seen = set()
    
    for char in text:
        # Ignore spaces
        if char == " ":
            continue
            
        if char in seen and char not in duplicates:
            duplicates.append(char)
        else:
            seen.add(char)
            
    return duplicates

print(find_duplicates("programming")) # Output: ['r', 'g', 'm']

"""
Tracking State: We create an empty list for our `duplicates` and an empty set called `seen` to remember what we've processed.
The Check: As we loop, we ask: "Have we seen this character before?"
If yes (and it's not already in our duplicates list), we add it to `duplicates`.
If no, we add it to our `seen` set
"""