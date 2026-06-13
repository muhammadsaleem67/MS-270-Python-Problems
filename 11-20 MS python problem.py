### Conditions
"""










"""

# 11. Check positive, negative, or zero.
values = int(input("Enter a number : "))
if values > 0 :
    print("it is positive.")
elif values < 0 :
    print("It is negative.")
else :
    print("It is 0.")

# 12. Check voting eligibility.
age = int(input("Enter your age : "))
if age > 18 :
    print("you can vote.")
else : 
    print("you are not eligible to vote.")

# 13. Check leap year.
year = int(input("Enter year : "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 :
    print("this is leap year!")
else :
    print("it is not leap year!")                                          

# 14. Check divisible by 5 and 11.
number = int(input("Enter a number : "))
if number % 5 == 0 :
    print("it is divisible by 5")
elif number % 11 == 0 :
    print("it is divisible by 11")
else :
    print("it is not divisible by neither 5 nor 11")
# 15. Check greatest between 2 numbers.
number1 = int(input("enter 1st number : "))
number2 = int(input("enter 2nd number : "))
if number1>number2 :
    print("numb1 is greater than numb2")
elif number2>number1 : 
    print("numb2 is greater than numb1")
elif number1 == number2 :
    print("numb1 is equal to numb2")

# 16. Check smallest among 3 numbers.
n1 = int(input("enter numb 1 : "))
n2 = int(input("enter numb 2 : "))
n3 = int(input("enter numb 3 : "))
if n1>n2 :
    small = n2 
elif n2>n3 :
    small = n3
else :
    small = n1
print("from",n1,n2,n3," values the ",small,"is smallest value ")

# 17. Grade calculator.
marks = int(input("enter the marks : "))
if marks > 80 :
    print("Grade : A1 ")
elif marks > 70 :
    print("Grade : A ")
elif marks > 60 :
    print("Grade : B ")
elif marks > 50 :
    print("Grade : C ")
elif marks > 40 :
    print("Grade : D ")
else :
    print("Fail!")

# 18. Check triangle validity.not complete
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))
if (a + b > c) and (a + c > b) and (b + c > a):
    print("Triangle is valid.")
else:
    print("Triangle is not valid.")

# 19. Check alphabet vowel or consonant.
alphabet = input("Enter an alphabet : ")
if alphabet == 'a' or alphabet == 'e' or alphabet == 'i' or alphabet == 'o' or alphabet == 'u' or alphabet == 'A' or alphabet == 'E' or alphabet == 'I' or alphabet == 'O' or alphabet == 'U' :
    print("it is Vowel! ")
else :
    print("it is Consonent! ")

# 20. Find absolute value manually. not complete
num = float(input("Enter a number: "))
if num < 0:
    absolute = -num
else:
    absolute = num
print("Absolute value is:", absolute) 