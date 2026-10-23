#Example 1: Input inside a function
def greet():
    name=input("Enter your name: ")
    print("Hello, " + name)
    return
greet()

#---------------------------------#-----------------------#-----------------------------
#Example 2: Input outside a function


def greet(name):
    print("Hello, " + name)
    return
user_name=str(input("Enter the name:"))
greet(user_name)