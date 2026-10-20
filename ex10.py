# Print the sum of numbers from 1 to N (N from user).

N = int(input("Enter a number:"))

sum = 0

for i in range(1,N+1):
    sum = sum + i

print("The sum of numbers from 1 to", N, "is:", sum)