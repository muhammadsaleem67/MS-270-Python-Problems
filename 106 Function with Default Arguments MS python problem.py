def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"
# Using the default argument
print(greet("Muhammad Saleem")) 
# Output: Hello, Alice!
# Overriding the default argument
print(greet("Babar", "Good morning")) 
# Output: Good morning, Bob!
"""
	1. Defining the Default: In the function definition def greet(name, greeting="Hello"):, we assign the string "Hello" directly to the parameter greeting.
	2. Omitting the Argument: When we call greet("Muhammad Saleem"), we only provide one piece of data. Python assigns "Alice" to name and automatically falls back to "Hello" for greeting.
	3. Overriding: When we call greet("Babar", "Good morning"), we provide both arguments. Python ignores the default "Hello" and uses "Good morning" instead.
"""
