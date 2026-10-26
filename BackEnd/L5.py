# Exercise 4 — Validate a login
# Write a function named check_login(username, password) with these rules:
# 1. If either username or password is empty, return "Fields are required".
# 2. If username is "admin" and password is "1234", return "Login successful".
# 3. Otherwise, return "Invalid username or password".
# Test it with one correct login, one incorrect password, and one empty field.



def check_login(username,password):
    if username == '' and password == '':
        return "Fields are required"
    elif username == "admin" and password == "1234":
        return "Login successful"
    else:
        return "Invalid username or password"

print(check_login("admin", "1234"))
