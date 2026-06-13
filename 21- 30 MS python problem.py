""""""










"""
# 21. Print numbers 1–100.
print("Printing 1-100!")
for i in range(0,101):
    print(i)

# 22. Print even numbers from 1–100.
print("Printing 1-100 even numbers")
for i in range(0,101):
    if i%2 == 0 :
        print(i)

# 23. Print odd numbers from 1–100.
print("Printing 1-100 odd numbers")
for i in range(0,101):
    if i % 2 == 0:
        continue
    else :
        print(i)

# 24. Sum of even numbers till n.
print("Print the sum of n numbers")
n = int(input("Enter number : "))+1
sum = 0
for i in range(0,n):
    sum = sum + i
print("All sum of",n-1,"is",sum)

# 25. Product of numbers from 1 to n.
print("Printing product of number from 1 to n.")
n = int(input("Enter number : "))+1
multiply = 1
for i in range(1,n):
    multiply = i*multiply
print(multiply)

# 26. Print reverse counting.
for i in range(10,0,-1):
    print(i)

# 27. Print squares from 1–20.
print("Printing square 1-20!")
for i in range(1,21):
    print(i,"Square :",i**2)

# 28. Print cubes from 1–20.
print("Printing Cube 1-20!")
for i in range(1,21):
    print(i, "Cube",i**3)

"""# 29. Count digits in number. not complete
print("digits : ")
digits = input("Enter digits : ")
# 4577
# 4 thousands 5 hundreds seventy seven
for i in range(len(digits)):
    if int(digits) > 1 and int(digits) < 1 :
        print(digits)
    elif int(digits) > 10 and int(digits) < 99 :
        print(digits)
    elif int(digits) > 100 and int(digits) < 999 :
        print(digits)
    elif int(digits) > 1000 and int(digits) < 9999 :
        print(digits)
    elif int(digits) > 10000 and int(digits) < 99999 :
        print(digits)
    elif int(digits) > 100000 and int(digits) < 999999 :
        print(digits)
    elif int(digits) > 100000 and int(digits) < 999999 :
        print(digits)
"""
for i in range(0,20):
    if digits[i] == 1 :
        print("One")
    elif digits[i] == 2 :
        print("Two")
    elif digits[i] == 3 :
        print("Three")
    elif digits[i] == 4 :
        print("Four")
    elif digits[i] == 5 :
        print("Five")
    elif digits[i] == 6 :
        print("Six")
    elif digits[i] == 7 :
        print("Seven")
    elif digits[i] == 8 :
        print("Eight")
    elif digits[i] == 9 :
        print("Nine")
    else :
        print("Not a Number")

"""
"""
# 30. Sum digits of a number.

numb = input("Enter a number : ")
numl = []
sum1 = 0
for i in range(len(numb)):
    numl.append(int(numb[i]))
    sum1 += numl[i]
    print(sum1)
print(sum1)"""