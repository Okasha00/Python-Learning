# Ask for a username and password. Print Login successful only if the username is admin and the\
#  password is 1234, otherwise Login failed.
#  (This is a nice mini-test-case idea: try valid and invalid combinations.)


username =input("Enter your username: ")

password = input("Enter your password:")

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Login failed")

    
