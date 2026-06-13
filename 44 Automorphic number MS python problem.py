def is_automorphic(num):
    square = num ** 2
    
    # Convert both to strings and check the ending
    return str(square).endswith(str(num))
print(is_automorphic(25)) # Output: True (625 ends with 25)
print(is_automorphic(7))  # Output: False (49 does not end with 7)
for i in range(10000000):
    square = i ** 2
    if str(square).endswith(str(i)):
        print("Automorph :",i)
