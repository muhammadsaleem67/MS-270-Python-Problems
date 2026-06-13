# 41. Armstrong number check.
print("Armstrong number check...")
def is_armstrong(numb):
    # convert number to string to easily iterate and find the lengh power
    numb_str = str(numb)
    power = len(numb_str)
    # sum the digits raised to calculated power
    total = sum(int(digit) ** power for digit in numb_str)
    return total == numb
print(is_armstrong(295245))
 # convert number to string to easily iterate and find the lengh power

numb = 56
numb_str = str(numb)
power = len(numb_str)
# sum the digits raised to calculated power
total = sum(int(digit) ** power for digit in numb_str)
print(total)
for i in range(100000):
    numb_str = str(i)
    power = len(numb_str)
    # sum the digits raised to calculated power
    total = sum(int(digit) ** power for digit in numb_str)
    # print(total)
    if i == total:
        print("Armstrong Number :", i)


"""
 	1. String Conversion: We convert num to a string (str(num)) so we can treat it as a list of individual characters and easily find out how many digits it has using len().
	2. List Comprehension & Math: int(digit) power converts each string character back to an integer and raises it to the power. The sum() function adds them all together.
	3. Comparison: We check if the calculated total matches the original num.

"""