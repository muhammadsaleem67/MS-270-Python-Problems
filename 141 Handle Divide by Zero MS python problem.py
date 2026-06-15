def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: You cannot divide a number by zero!"
print(safe_divide(10, 2))
print(safe_divide(10, 0))
"""
	1. The try Block: Python attempts to execute the code inside this block. If it works, it skips the except block entirely.
	2. The except Block: If a ZeroDivisionError occurs inside the try block, Python immediately stops what it's doing and jumps to this block instead of crashing the program.
"""