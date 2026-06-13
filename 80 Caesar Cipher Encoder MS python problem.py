def caesar_cipher(text, shift):
    encoded = ""
    
    for char in text:
        if char.isupper():
            # Shift uppercase letters (ASCII 65 to 90)
            shifted = (ord(char) - 65 + shift) % 26 + 65
            encoded += chr(shifted)
        elif char.islower():
            # Shift lowercase letters (ASCII 97 to 122)
            shifted = (ord(char) - 97 + shift) % 26 + 97
            encoded += chr(shifted)
        else:
            # Leave spaces and punctuation alone
            encoded += char
            
    return encoded
print(caesar_cipher("Hello World!", 3)) 
"""
	1. Checking Case: We check if the character is uppercase or lowercase using .isupper() and .islower(), because their ASCII number ranges are different.
	2. The Math (Normalization): * Let's take an uppercase 'A' (ASCII 65).
		○ ord(char) - 65 turns 'A' into 0, 'B' into 1, 'Z' into 25. This gives us a clean 0-25 scale.
	3. The Shift & Modulo: We add our shift amount. If we shift 'Z' (25) by 1, it becomes 26. We use modulo 26 (% 26) to force it to wrap around back to 0.
	4. Back to ASCII: We add 65 back to our result to put it back in the uppercase ASCII range, and use chr() to convert that number back into a readable letter.
	5. Preservation: If the character isn't a letter (like a space or exclamation mark), we just append it as-is.
"""