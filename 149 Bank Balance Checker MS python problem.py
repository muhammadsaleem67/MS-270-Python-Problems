class MinimumBalanceError(Exception):
    pass
def check_balance_transfer(current_balance, transfer_amount):
    MINIMUM_REQUIRED = 50    
    try:
        resulting_balance = current_balance - transfer_amount        
        if resulting_balance < MINIMUM_REQUIRED:
            raise MinimumBalanceError(f"Transfer blocked. Balance cannot drop below ${MINIMUM_REQUIRED}.")            
        return f"Transfer complete. Remaining balance: ${resulting_balance}"        
    except MinimumBalanceError as error:
        return str(error)
print(check_balance_transfer(200, 100)) # Output: Transfer complete. Remaining balance: $100
print(check_balance_transfer(100, 80))  # Output: Transfer blocked. Balance cannot drop below $50.
"""
	1. Constants: MINIMUM_REQUIRED = 50 acts as our business rule.
	2. Pre-computation Check: We calculate what the balance would be before actually modifying any real data. If the resulting balance breaks the rule, we raise the exception to block the transaction.
"""