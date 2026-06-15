inventory = {}
def update_inventory(item, quantity):
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity
def view_inventory():
    print("--- Current Stock ---")
    for item, qty in inventory.items():
        print(f"{item.title()}: {qty}")
# Simulating operations
update_inventory("apples", 50)
update_inventory("oranges", 20)
update_inventory("apples", -10) # Sold 10 apples
view_inventory()
# Output:
# --- Current Stock ---
# Apples: 40
# Oranges: 20
