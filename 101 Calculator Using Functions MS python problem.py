def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero!"
    x / y
def calculator(operation, num1, num2):
    # A dictionary mapping symbols to their respective functions
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }
    
    # .get() fetches the function. If the symbol isn't found, it returns None
    func = operations.get(operation)
    
    if func:
        return func(num1, num2)
    else:
        return "Invalid operation symbol."
print(calculator('+', 10, 5)) # Output: 15
print(calculator('/', 10, 0)) # Output: Error: Cannot divide by zero!
"""
	1. Operation Functions: We define simple, single-purpose functions for addition, subtraction, multiplication, and division. The division function includes a safety check to prevent program crashes if a user tries to divide by zero.
	2. The Dispatcher (calculator): This is our main function. It takes the mathematical symbol and the two numbers.
	3. Dictionary Mapping: We create a dictionary where the keys are string symbols ('+', '-') and the values are the actual functions themselves (e.g., add without the parentheses). In Python, functions are first-class objects, meaning you can pass them around like variables.
	4. Execution: We look up the symbol in the dictionary, retrieve the correct function, and pass num1 and num2 into it.
"""