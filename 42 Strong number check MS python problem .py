# 42. Strong number check.
import math
def is_strong_number(num):
    num_str = str(num)
    # Sum the factorial of each digit
    total = sum(math.factorial(int(digit)) for digit in num_str)    
    return total == num
print(is_strong_number(145)) # Output: True
for i in range(100000):
        num_str = str(i)
        # Sum the factorial of each digit
        total = sum(math.factorial(int(digit)) for digit in num_str)
        if i == total :
              print("Strong Number : ",i)
        
        

"""
	1. Import Math: We bring in Python's built-in math module to use math.factorial(), saving us from writing our own factorial loop.
	2. String Conversion: Just like the Armstrong problem, we convert the number to a string to easily pull out individual digits.
	3. Summing Factorials: We loop through each digit, calculate its factorial, sum them up, and check if the total equals the original number.
"""