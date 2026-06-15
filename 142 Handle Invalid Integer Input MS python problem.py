def get_age(input_string):
    try:
        age = int(input_string)
        return f"You are {age} years old."
    except ValueError:
        return "Invalid input! Please enter numbers only."
print(get_age("25"))     # Output: You are 25 years old.
print(get_age("twenty")) # Output: Invalid input! Please enter numbers only.
