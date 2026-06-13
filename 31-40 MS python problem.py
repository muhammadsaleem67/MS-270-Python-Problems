"""







"""
"""
31. Print:

```python
*
**
***
****
```
"""
print("Triangle")
for i in range(0,5):
    for j in range(0,i+1):
        print("*",end="")
    print()

# 32. Print inverted triangle.
print("inverted triangle.")
for i in range(5,-1,-1):
    for j in range(i+1,0,-1):
        print("*", end="")
    print()
print("*"*40)
def inverted_triangle(rows):
    for i in range(rows, 0, -1):
        print("*" * i)
inverted_triangle(5)
print("Inverted Triangle")
def inverted_triangle(rows):
    # Outer loop controls the rows (counting down)
    for i in range(rows, 0, -1):
    # Inner loop controls how many stars to print on the current row
        for j in range(i):
            print("*", end=" ")
        print() # Move to the next line after the inner loop finishes
inverted_triangle(5)

# 33. Print pyramid pattern. not complete
print("Pyramid pattern")
for i in range(0,5):
    for j in range(0,5):
        print("*", end=" ")
    print()
def pyramid(rows):
    for i in range(1, rows + 1):
        spaces = " " * (rows - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)
print("-"*40)
print("Pyramid pattern")
def pyramid(rows):
# Outer loop for rows
    for i in range(1, rows + 1):
        
        # Inner loop 1: Print leading spaces
        for j in range(rows - i):
            print(" ", end="")
            
        # Inner loop 2: Print the stars
        for j in range(2 * i - 1):
            print("*", end="")
            
        print() # Move to the next line
pyramid(5)



# 34. Print Floyd’s triangle. not complete
print("Floyd's traingle")
def floyds_triangle(rows):
    number = 1
    for i in range(1,rows+1):
        for j in range(1, i+1):
            print(number, end="")
            number += 1
        print()
floyds_triangle(5)
# 35. Print multiplication triangle.
"""
1
1 4
1 4 9
1 4 9 16
1 4 9 16 25
"""
print("multiplication triangle.")
for i in range(0,5):
    for j in range(0,i+1):
        print(j**2, end = " ")
    print()
def multiplication_triangle(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(i * j, end="\t")
        print()
multiplication_triangle(5)

# 36. Print hollow square.
print("Hollow Square...")
def hollow_square(size):
    for i in range(size):
        for j in range(size):
            if i == 0 or i == size - 1 or j == 0 or j == size - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
hollow_square(5)

# 37. Print diamond pattern.
print("Diamond Pattern")
def diamond(rows):
    # Top Half
    for i in range(1, rows + 1):
        for j in range(rows - i):
            print(" ", end="")
        for j in range(2*i-1):
            print("*", end="")
        print()
    
    for i in range(rows-1, 0, - 1):
        for j in range(rows -i):
            print(" ", end="")
        for j in range(2*i - 1):
            print("*", end="")
        print()
diamond(5)
# 38. Print X pattern using stars.
print("-"*40)
print("X pattern using stars...")
def x_pattern(size):
    for i in range(size):
        for j in range(size):
            if i == j or i + j == size - 1:
                print("*", end="")
            else :
                print(" ", end="")
        print()
x_pattern(5)

# 39. Print checkerboard pattern.
print(" Checker Bourd pattern...")
def checkerboard(size):
    for i in range(size):
        for j in range(size):
            if (i + j) % 2 == 0:
                print("*", end=" ")
            else :
                print(" ", end=" ")
        print()
checkerboard(5)
# 40. Print alphabet pyramid.
"""
    a
   bcd
  efghi
 jklmnop
qrstuvwxy
z
"""
print("Alphabetic Pyramid...")
def alphabet_pyramid(rows):
    for i in range(1, rows + 1):
        for j in range(rows - i):
            print(" ", end="")
        for j in range(i):
            print(chr(65 + j), end=" ")
        print()
alphabet_pyramid(5)

k = 0
alphabet = "abcdefghijklmnopqrstuvwxyz"
for i in range(0,5):
    for j in range(0,9):
        k += 1
        print(alphabet[j], end= " ")
    print()

for i in range(0,26):
    if i == len(alphabet)/2:
        print(alphabet[i], end = " ")