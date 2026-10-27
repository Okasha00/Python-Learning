# Exercise 1 — Discount Calculator
# Ek shop par customer ko bill ke mutabiq discount milta hai.

# Requirements:
# 1. User se total bill input lo.
# 2. Agar bill 5000 ya zyada ho, to 10% discount do.
# 3. Warna discount nahi milega.
# 4. Final bill print karo.
# 5. Agar bill zero ya negative ho, `"Invalid


# 1. User se total bill input lena (float numbers ke liye)
try:
    total_bill = float(input("Apna total bill enter karein: "))

    # 5. Agar bill zero ya negative ho
    if total_bill <= 0:
        print("Invalid bill")

    else:
        # 2. Agar bill 5000 ya zyada ho, to 10% discount
        if total_bill >= 5000:
            discount = total_bill * 0.10
            final_bill = total_bill - discount
        # 3. Warna discount nahi milega
        else:
            final_bill = total_bill

        # 4. Final bill print karo
        print(f"Aapka final bill hai: Rs. {final_bill}")

except ValueError:
    print("Invalid bill (Sahi number enter karein)")
