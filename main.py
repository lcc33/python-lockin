full = input("enter your username: ")
age = int(input("enter your age: "))
if full == "aizen":
    print("pls send " +  full[0:].upper() + " money!!($100000), " f"he is just {age} years old!!")
else:
  print("where is aizen??")
print("welcome user pls login")
email = input("enter email: ")
password = input("enter password: ")
if email == "uweh@gmail.com" and  password == "uweh":
   print(f"yokoso {full} you are logged in as {email} and your password is {password}" )
else:
    print("sorry user cannot be found!")