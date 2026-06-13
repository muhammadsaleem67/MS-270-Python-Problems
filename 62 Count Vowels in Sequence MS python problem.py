def count_vowels(text):
    # Define what we are looking for
    vowels = "aeiouAEIOU"
    count = 0
    
    for char in text:
        if char in vowels:
            count += 1
            
    return count

print(count_vowels("Hello World")) # Output: 3
"""
1. The Reference: We create a string containing both lowercase and uppercase vowels so our function is case-insensitive.
2. The Loop: We iterate through every single character in the input `text`.
3. The Check: if char in vowels:` asks Python to check if the current letter exists anywhere inside our reference string. If it does, we add 1 to our count.
"""