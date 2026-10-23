
def greet():
    a=str(input("Enter your First name: "))
    b=str(input("Enter your Last name: "))
    return a+b
user = greet()
print("Welcome, " + user)


#-----------------------------------------#------------------------------#----

def get_sum():
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    return a+b
S=get_sum()
print("The sum is:", S)