def manual_uppercase(text):
    result = ""
    
    for char in text:
        # Check if the character is a lowercase letter (a-z)
        if 'a' <= char <= 'z':
            # Find its ASCII number, subtract 32, and turn it back into a letter
            upper_char = chr(ord(char) - 32)
            result += upper_char
        else:
            # If it's already uppercase, a number, or punctuation, leave it alone
            result += char
            
    return result

print(manual_uppercase("hello world 123!")) # Output: HELLO WORLD 123!
"""
ASCII Logic: In computer memory, 'a' is the number 97, and 'A' is 65. 'b' is 98, and 'B' is 66. The uppercase version of *any* letter is exactly 32 less than its lowercase version.
`ord()`: This function takes a character and gives you its hidden ASCII number.
The Math: We subtract 32 from that number to find the uppercase equivalent.
`chr()`: This function takes a number and turns it back into a readable character.
"""