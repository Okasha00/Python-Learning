# Exercise 10 — Shopping cart
# Requirements
# 1. User se product price aur quantity input lo.
# 2. Agar price ya quantity 0 ya us se kam ho, "Invalid input" return karo.
# 3. Subtotal = price * quantity.
# 4. Agar subtotal 5000 ya zyada ho, 10% discount do.
# 5. Agar subtotal 5000 se kam ho, Rs. 200 shipping charge add karo.
# 6. Final bill return karo.

def calculate_final_bill(price, quantity):

    if price <= 0 or quantity <= 0:
        return "Invalid input"
    Subtotal = price * quantity

    if Subtotal < 5000:
        discount=0.10
        final_bill = Subtotal - discount
        
    elif Subtotal > 5000:
        shipping = 200
        final_bill = Subtotal + shipping

    return  final_bill

price = int(input("Enter the price: "))
quantity = int(input("Enter the quantity: "))

print("Final bill:", calculate_final_bill(price, quantity))

    