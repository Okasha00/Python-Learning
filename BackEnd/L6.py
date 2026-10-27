# Exercise 5 — Calculate the shopping cart total
# Write a function calculate_cart_total(price, quantity) with these rules:
# 1. If price <= 0 or quantity <= 0, return "Invalid input".
# 2. Otherwise, calculate and return price * quantity.
# Test it with calculate_cart_total(1000, 3) and calculate_cart_total(1000, 0)



def calculate_cart_total(price, quantity):
    if price <=0 or quantity <= 0:
        return "Invalid Input"
    else:
        return price * quantity

print(calculate_cart_total(1000,3))
print(calculate_cart_total(1000, 0))