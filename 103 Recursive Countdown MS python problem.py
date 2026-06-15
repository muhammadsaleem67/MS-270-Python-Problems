def countdown(n):
    # Base Case: When to stop
    if n <= 0:
        print("Blastoff!")
        return
        
    # Action
    print(n)
    
    # Recursive Call: Call the same function with a smaller payload
    countdown(n - 1)
countdown(5)
"""
	1. The Base Case: Before doing anything, the function checks if n has reached 0. If it has, it prints "Blastoff!" and hits return, which safely stops the recursion.
	2. The Action: If n is greater than 0, it prints the current number.
	3. The Recursion: The function then calls itself, but passes n - 1 into the new call. If you start with 5, the next call gets 4, then 3, continuously stepping down until the base case is triggered.
"""