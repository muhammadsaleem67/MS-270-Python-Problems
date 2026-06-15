class InsufficientFundsError(Exception):
    pass
def withdraw(balance, amount):
    try:
        if amount > balance:
            raise InsufficientFundsError(f"Cannot withdraw ${amount}. Current balance is ${balance}.")
        new_balance = balance - amount
        return f"Withdrawal successful. New balance: ${new_balance}"
    except InsufficientFundsError as error:
        return str(error)
print(withdraw(100, 40))  # Output: Withdrawal successful. New balance: $60
print(withdraw(100, 150)) # Output: Cannot withdraw $150. Current balance is $100.
"""
	1. Domain-Specific Error: InsufficientFundssError makes it immediately clear to other programmers exactly what business logic failed.
	2. Error Messages: When we raise the error, we pass a customized string into it. We extract that string in the except block using as error and return it.
"""