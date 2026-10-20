# Print the multiplication table of a number entered by the user (e.g. 5 x 1 = 5 ... 5 x 10 = 50).

number = int(input("Enter a number: "))

for i in range(1,11):
    result = number * i
    print(number , "x" ,i , "=", result)