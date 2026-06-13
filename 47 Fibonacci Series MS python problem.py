def fibonacci(num):
    if num <= 0 :
        return []
    elif num == 1:
        return [0]
    sequence = [0,1]
    # loop to generate the remaining numbers
    for i in range(2, num):
        nextnum = sequence[-1]+sequence[-2]
        sequence.append(nextnum)
    return sequence
inputnumber = int(input("Enter A Number"))
print(fibonacci(inputnumber))

"""
	1. Base Cases: If the user asks for 0 terms, we return an empty list. If they ask for 1 term, we return [0].
	2. Starting Sequence: We initialize the list with the first two numbers: [0, 1].
	3. The Loop: We loop from 2 up to n. In Python lists, sequence[-1] grabs the last item, and sequence[-2] grabs the second-to-last item. We add them together and append the new number to the list.

"""