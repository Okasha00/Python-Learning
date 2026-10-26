# Exercise 3
# Check product stock

# A store has a certain quantity of a product in stock.

# Create a function place_order(stock, quantity).

# Business rules:
# - If quantity is less than or equal to 0, return "Invalid quantity".
# - If quantity exceeds stock, return "Insufficient stock".
# - Otherwise, return "Order placed".
# Examples:
# - place_order(10, 3) → "Order placed"
# - place_order(10, 15) → "Insufficient stock"
# - place_order(10, 0) → "Invalid quantity"

def place_order(stock, quantity):
    if quantity <= 0 :
        return "Invalid Quantity"
    elif quantity > stock:
        return "Insufficient stock"
    else:
        return "Order placed"

print(place_order(10, 15))
print(place_order(10, 3))
print(place_order(10, 0))