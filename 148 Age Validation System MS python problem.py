class InvalidAgeError(Exception):
    pass
def register_user(age):
    try:
        if not isinstance(age, int):
            raise ValueError("Age must be a number.")
        if age < 0 or age > 120:
            raise InvalidAgeError("Age must be between 0 and 120.")            
        return "User registered."        
    except (ValueError, InvalidAgeError) as error:
        return f"Registration Failed: {error}"
print(register_user(25))    # Output: User registered.
print(register_user(-5))    # Output: Registration Failed: Age must be between 0 and 120.
print(register_user("ten")) # Output: Registration Failed: Age must be a number.
