password = input("Password:")
while True:
    reppassword = input("Repeat password:")
    if reppassword != password:
        print("They do not match!")
    if reppassword == password:
        break
print("User account created!")
