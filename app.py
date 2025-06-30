print("welcome to Keynest!")
users = int(input("how many users were active today? "))
print(f"you had {users} users today admin")


def store_credentials():
  platform = input("platform name: ")
  username = input("username: ")
  password = input("password: ")
  print(f" platform: {platform} \n username: {username}  \n password: {password} ")
if users == 10:
  store_credentials()
else:
    print("omo u need to login first to save credentials!")