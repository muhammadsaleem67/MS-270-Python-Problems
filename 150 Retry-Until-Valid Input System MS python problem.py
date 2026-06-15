def get_valid_integer():
    # Simulate user input using a predefined list for demonstration
    simulated_inputs = ["hello", "", "3.14", "42"]    
    for user_input in simulated_inputs:
        try:
            print(f"User typed: '{user_input}'")
            # Try to convert to integer
            valid_number = int(user_input)            
            # If successful, return and break the loop
            print("Success!")
            return valid_number            
        except ValueError:
            print("Invalid input. Please try again.\n")
# Run the system
final_answer = get_valid_integer()
print(f"The valid integer is: {final_answer}")
