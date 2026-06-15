# Create the custom exception
class NegativeNumberError(Exception):
    pass
def check_positive(number):
    try:
        if number < 0:
            # Use the 'raise' keyword to trigger our custom error manually
            raise NegativeNumberError("Negative numbers are not permitted here.")
        return "Valid number!"
    except NegativeNumberError as error:
        return str(error)
print(check_positive(5))  # Output: Valid number!
print(check_positive(-2)) # Output: Negative numbers are not permitted here.
"""
	1. Inheritance: class NegativeNumberError(Exception): tells Python: "Create a new class, and give it all the powers and behaviors of the standard Exception object."
	2. The raise Keyword: While Python throws standard errors automatically, you must use raise to manually trigger your custom errors when a specific condition is met.
"""