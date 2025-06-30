count = 0
while count < 5:
    print("Yokoso!")
    count += 1
users = 0
while users < 3:
    username = input("enter your username: ")
    users += 1
    print(username)

attempt = 0
while attempt < 3:
    email = input("enter email id: ")
    password = input("enter password: ")
    if email and password:
        print("Login successful")
    attempt += 1