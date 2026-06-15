class MaxRetriesExceededError(Exception):
    pass
def simulate_login(password_attempts):
    correct_password = "secure123"    
    try:
        for attempt, guess in enumerate(password_attempts, 1):
            if guess == correct_password:
                return "Login successful!"            
            if attempt >= 3:
                raise MaxRetriesExceededError("Account locked. Too many failed attempts.")                
        return "Login failed."    
    except MaxRetriesExceededError as error:
        return str(error)
print(simulate_login(["password", "123456", "admin"])) 
# Output: Account locked. Too many failed attempts.
"""
	1. Tracking State: We loop through a list of simulated guesses, using enumerate to count which attempt we are currently on.
	2. The Threshold: Once attempt hits 3, we immediately raise our custom security exception, halting the loop and preventing any further guesses.
"""