def validate_password(password):
    # 1. Check length
    if len(password) < 8:
        return False
    # Variables to track our requirements
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    
    # 2. Iterate through once and flag what we find
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif not char.isalnum():
            # If it's not a letter or a number, it's a special character
            has_special = True
            
    # 3. Ensure all conditions are True
    return has_upper and has_lower and has_digit and has_special
print(validate_password("weakpass"))      # Output: False
print(validate_password("Strong!Pass1"))  # Output: True
"""
	1. Quick Exit: We immediately check the length. If it's under 8 characters, we can stop processing and return False right away to save time.
	2. State Flags: We set four boolean flags to False. These act as a checklist.
	3. Single-Pass Evaluation: We loop over every character exactly once. We use Python's built-in string methods (.isupper(), .islower(), .isdigit()) to inspect the character. If .isalnum() (is alphanumeric) is false, it guarantees we are looking at a special symbol like ! or @. We flip the corresponding flags to True.
	4. Final Verdict: We use the and operator to combine all our flags. It will only return True if every single requirement flag was flipped during the loop.
"""