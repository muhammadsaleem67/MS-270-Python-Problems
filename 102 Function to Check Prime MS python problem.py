def is_prime(num):
    # handle base cases immediately
    if num <= 1:
        return False
    if num == 2:
        return True
    # eliminate all even numbers to speed up the loop 
    if num % 2 == 0:
        return False
    # check odd numbers up to the square root of number
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True
print(is_prime(8))
    
