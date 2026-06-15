def is_palindrome_recursive(text):
    # Convert to string and lowercase to handle numbers or mixed cases
    text = str(text).lower()
    
    # Base Case: A string of 0 or 1 characters is always a palindrome
    if len(text) <= 1:
        return True
        
    # Check if the first and last characters match
    if text[0] != text[-1]:
        return False
        
    # Recursive Call: Pass the string without the first and last characters
    return is_palindrome_recursive(text[1:-1])
print(is_palindrome_recursive("Racecar")) # Output: True
print(is_palindrome_recursive("Python"))  # Output: False
"""
	1. Normalization: We convert the input to a lowercase string so "Racecar" perfectly matches "racecar".
	2. The Base Case: If the string length is reduced to 1 or 0 (meaning we've checked all pairs without failing), it is officially a palindrome.
	3. The Edge Check: We compare text[0] (the very first character) with text[-1] (the very last character). If they don't match, the word is not a palindrome, and we immediately return False.
	4. The Recursive Slice: If the outer letters do match, we slice them off using text[1:-1] (which removes the first and last characters) and pass the smaller, inner string back into the function to repeat the process.
"""