"""








"""
# 1. Print your favorite quote.
print("as you sow so shall you reap.")

# 2. Print your age after 10 years.
age = 21 
print("age :", age, "My age after 10 years is : ", age+10)

# 3. Take user age and print months lived.
user_age = int(input("Enter you age : "))
months = user_age*12
print("You are", months, "months old")

# 4. Swap two numbers using a third variable.
x = 7
y = 8
print(x,",",y)
temp = y
y = x
x = temp
print(x,",",y)

# 5. Swap two numbers without third variable.
a = 8
b = 7
a = a + b
b = a - b
a = a - b
print("a =",a, "b =",b)
x = y
y = x
print(x,",",y)

# 6. Convert kilometers to meters.
Km = int(input("Enter kms : "))
meter = Km*1000
print(Km,"Kms are equal to",meter,"Meters")

# 7. Convert minutes into hours and minutes.
minutes = int(input("Enter Minute : "))
hours = int(minutes/60)
remain_mins = +(minutes-(hours*60))
print(minutes, "minutes are equal to", hours,":",remain_mins)

# 8. Find square and cube of a number.
number = int(input("Enter a number : "))
square = number**2
cube = number**3
print("Number :",number,"Square :",square,"Cube :",cube)

# 9. Calculate simple interest.
loan = int(input("Enter how loan : "))
interest = 5/100
print(loan, "you have to pay", loan,"with interest",int(interest*loan),"this years last month")

# 10. Calculate area of rectangle.
print("Calculate Area of Rectangle. ")
length = int(input("Enter the length : "))
width = int(input("Enter the width : "))
area = length*width
print("Area of rectangle :",area)
