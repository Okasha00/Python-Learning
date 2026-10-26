def check_even(n):
    if n % 2 == 0:
        return "Even number"
    else:
        return "Odd number"

# This will now work perfectly without printing "None"
print(check_even(7))
