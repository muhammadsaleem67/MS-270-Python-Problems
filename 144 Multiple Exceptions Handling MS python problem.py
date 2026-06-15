def divide_from_input(a_str, b_str):
    try:
        a = int(a_str)
        b = int(b_str)
        return a / b
    except ValueError:
        return "Error: Please provide valid integers."
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
print(divide_from_input("10", "apple")) # Output: Error: Please provide valid integers.
print(divide_from_input("10", "0"))     # Output: Error: Division by zero is not allowed.
"""
	1. Multiple Failure Points: The code can fail during int() conversion (ValueError) OR during the / division (ZeroDivisionError).
	2. Sequential Checking: Python checks the except blocks from top to bottom. It executes the first one that matches the error and ignores the rest.
"""