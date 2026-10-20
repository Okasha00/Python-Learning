# Ask for a number and print its factorial (5! = 5x4x3x2x1).



number = int(input("Enter the number:"))

factrial = 1

for i in range(1, number+1):
    factrial = factrial * i 

print("The factorial of", number, "is:", factrial)