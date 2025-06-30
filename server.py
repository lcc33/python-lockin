print("welcome to admin dashboard!")
email = input("enter your email id: ")
password = input("enter your password: ")
def routing():
    server = input("enter endpoint (e.g. /login, /signup): ")
    if server == "/login":
        print("logging in..")
    elif server == "/signup":
        print("creating account..")
    elif server == "/forgot":
        print("reset link sent.")
    else:
        print("404 not found")
if email == "admintrace@gmail.com" and password == "vault":
    print("Welcome back admin")
    routing()
else:
    print("Access denied!")
