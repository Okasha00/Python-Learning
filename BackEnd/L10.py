# Exercise 9 — Order status validation
# Ab thori different business logic practice karte hain.

# Function ka naam check_order_status(status) rakho.

# Requirements:
# 1. Agar status == "Pending" ho, return "Order is waiting for processing".
# 2. Agar status == "Processing" ho, return "Order is being prepared".
# 3. Agar status == "Completed" ho, return "Order delivered successfully".
# 4. Agar inke ilawa koi status ho, return "Invalid order status".

def check_order_status(status):
    if status == "Pending":
        return "Order is waiting for processing"
    elif status == "Processing":
        return "Order is being prepared"
    elif status == "Completed":
        return "Order delivered successfully"
    else:
        return "Invalid order status"
print(check_order_status("Pending"))
print(check_order_status("Processing"))
print(check_order_status("Completed"))
print(check_order_status("Cancelled"))          