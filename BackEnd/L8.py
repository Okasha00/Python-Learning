# Exercise 7 — Calculate order total
# Ek online shop mein customer product ki price aur quantity enter karta hai.

# Rules:
# 1. Agar price <= 0 ya quantity <= 0 ho, return "Invalid input".
# 2. Agar subtotal 5000 ya us se zyada ho, 10% discount apply karo.
# 3. Warna original subtotal return karo.
# Example: price = 2000, quantity = 3

# Subtotal = 6000, discount = 600, final total = 5400.

def calculate_order_total(price, quantity):
    subtotal = price * quantity
    if price <=0 or quantity <= 0:
        return "invalid input"

    subtotal = price * quantity
    if subtotal < 5000:
        return subtotal * .10
    else:
        return subtotal

print(calculate_order_total(2000,3))