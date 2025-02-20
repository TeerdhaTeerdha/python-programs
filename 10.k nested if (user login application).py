# write a program for the user login
user=input("Enter the username: ")
password=input("Enter the password: ")
if user == "python":
    if password == "py123":
        print("Welcome to python world")
    else:
        print("invalid password")
else:
    print("invalid username")
