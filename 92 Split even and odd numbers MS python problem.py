def split_even_odd(lst):
    # Using list comprehensions for clean, readable code
    evens = [x for x in lst if x % 2 == 0]
    odds = [x for x in lst if x % 2 != 0]
    
    return evens, odds
even_list, odd_list = split_even_odd([1, 2, 3, 4, 5, 6, 7])
print(f"Evens: {even_list}, Odds: {odd_list}")
# Output: Evens: [2, 4, 6], Odds: [1, 3, 5, 7]
