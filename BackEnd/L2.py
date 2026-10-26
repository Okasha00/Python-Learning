# Exercise 1
# Validate an order quantity

# Create a function check_quantity(quantity).

# Business rules:
# - If quantity is greater than 0, return "Valid quantity".
# - Otherwise, return "Invalid quantity".
# Examples: check_quantity(3) → "Valid quantity"; check_quantity(0) → "Invalid quantity".



def check_quantity(quantity):
    if quantity > 0:
        return "Valid Quantity"
    else: 
        return "invalid Quantity"

print(check_quantity(5))