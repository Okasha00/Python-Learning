# Lesson 1: Calculate a shopping bill
# Imagine a store sells a laptop for Rs. 80,000. 
# A customer buys two laptops. Your job is to calculate the total bill.


print("Bill Calculation")

Qty=int(input("Enter the Quantity:"))
price = int(input("Enter the Price:"))



bill = Qty * price
discount = 0 
if bill > 500:
    discount = bill * 0.12
    bill = bill - discount
    
print("Total bill is:",bill,"PKR", "The Discount is:",discount,"PKR")