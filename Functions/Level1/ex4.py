# Q4
# Return a value

# Create a function add(a, b) that returns the sum of two numbers. Store the returned value in a variable and print it.

# Example: add(5, 3) → 8



def add():
    a=int(input("Enter the first number: "))    
    b=int(input("Enter the second number: "))
    return a+b
S=add()
print("The sum is:", S)