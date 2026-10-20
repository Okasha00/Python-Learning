name = "Ali"            # variable (string)
age = 25                # integer
print("Hello", name)    # output

city = input("City? ")  # input ALWAYS returns a string
age = int(input("Age? "))  # convert to number with int()

if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teen")
else:
    print("Child")



