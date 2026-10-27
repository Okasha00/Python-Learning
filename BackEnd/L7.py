# Exercise 6 — Check product availability
# Now let's make the business logic slightly harder.

# Write a function called check_product_availability(stock, requested_quantity).
# Rules:
# 1. If stock < 0 or requested_quantity <= 0, return "Invalid input".
# 2. If stock == 0, return "Out of stock".
# 3. If requested_quantity > stock, return "Not enough stock".
# 4. Otherwise, return "Product available".
# Test these calls:
# print(check_product_availability(10, 3))print(check_product_availability(10, 15))print(check_product_availability(0, 2))print(check_product_availability(10, 0))

# Hint: The order of your if and elif conditions matters. Validate the inputs first, then check stock availability.

def check_product_availability(stock, requested_quantity):
    if stock < 0 or requested_quantity <=0:
        return "Invalid Input"
    elif stock == 0:
        return "Out Of Stock"
    elif requested_quantity > stock:
        return "Not enough stock"
    else:
        return "Product avaiable"
    
print(check_product_availability(10, 3))
print(check_product_availability(10, 15))
print(check_product_availability(0, 2))
print(check_product_availability(10, 0))