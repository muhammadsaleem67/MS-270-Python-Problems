def fibonacci_recursive(n):
    # Base Cases
    if n <= 0:
        return 0
    if n == 1:
        return 1
        
    # Recursive Call
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
print(fibonacci_recursive(8
                          )) # Output: 8
