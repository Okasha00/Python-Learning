# Exercise 8 — Calculate shipping charges
# Ek online shopping website par shipping charges order ke total par depend karte hain.

# Requirements:
# 1. Agar total <= 0 ho, return "Invalid total".
# 2. Agar total >= 5000 ho, shipping free hai.
# 3. Agar total < 5000 ho, shipping charges Rs. 200 hain.
# 4. Function ko order total + shipping charges return karne hain.

def calculate_shipping(total):
   
    if total <=0:
        return "Invalid Input"
    elif total >= 5000:
        shipping = 0
    else:
        shipping = 200

    return total + shipping
    
print(calculate_shipping(3000))