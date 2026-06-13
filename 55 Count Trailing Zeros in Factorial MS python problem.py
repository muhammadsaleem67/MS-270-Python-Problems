def trailing_zeros(num):
    if num < 0:
        return 0
    count = 0
    # keep dividing by powers of 5
    while num >= 5:
        num //= 5 
        count += num

    return count
print(trailing_zeros(100))
