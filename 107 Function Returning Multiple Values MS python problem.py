def math_operations(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    
    # Return all three results separated by commas
    return addition, subtraction, multiplication
# Unpacking the returned values into separate variables
add_result, sub_result, mult_result = math_operations(10, 5)
print(f"Sum: {add_result}, Difference: {sub_result}, Product: {mult_result}")
# Output: Sum: 15, Difference: 5, Product: 50
"""
	1. The Return Statement: By separating variables with commas (return addition, subtraction, multiplication), Python secretly bundles them into a single data structure called a tuple.
	2. Unpacking: When we call the function, we can provide three comma-separated variable names on the left side of the equals sign (add_result, sub_result, mult_result = ...). Python perfectly maps the three returned values to these three distinct variables.
"""