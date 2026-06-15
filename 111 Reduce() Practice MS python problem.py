from functools import reduce
def calculate_total_product(numbers):
    # reduce takes a function (lambda) and a sequence (numbers)
    result = reduce(lambda x, y: x * y, numbers)
    return result
print(calculate_total_product([1, 2, 3, 4, 5])) 
# Output: 120 (1*2*3*4*5)
