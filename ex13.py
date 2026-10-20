# Ask for a number and count how many digits it has (use while and // 10).

number = int(input("Enter the number:"))


count = 0

while number > 0:
    number = number //10
    count +=1

print("The number of digits in the number is:", count)

