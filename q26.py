username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin":
    if password == "1234":
        print("Login successful\n")
    else:
        print("Invalid password\n")
else:
    print("Invalid username\n")