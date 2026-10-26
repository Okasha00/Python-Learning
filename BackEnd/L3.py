# Exercise 2
# Apply a shopping discount

# Create a function calculate_discount(total).

# Business rules:
# - If the total is at least Rs. 5,000, apply a 10% discount.
# - Otherwise, return the original total.
# Examples: calculate_discount(6000) → 5400; calculate_discount(3000) → 3000.

# Concepts: calculations, conditions, return.


def calculate_discount(total):
    if total >= 5000:
        discount = total * 0.10
        final_total = total - discount
        return final_total
    else:
        return total


#total = int(input("Enter the total:"))
print(calculate_discount(4000))