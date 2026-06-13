def is_anagram(str1, str2):
    # Clean up the strings: remove spaces and make lowercase
    clean_str1 = str1.replace(" ", "").lower()
    clean_str2 = str2.replace(" ", "").lower()
    
    # Sort them alphabetically and compare
    return sorted(clean_str1) == sorted(clean_str2)

print(is_anagram("Listen", "Silent")) # Output: True
print(is_anagram("Hello", "World"))   # Output: False
