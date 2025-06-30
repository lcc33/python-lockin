# Ask user: How many months do you want to subscribe?
# Price is ₦500 per month
# Calculate total
# If the months is more than 12, give a 20% discount
# Print final price

print("welcome to kindra hub")
price = 500
month = int(input("how many months do you wish to subscribe for? "))
total = int(price * month)
def calculate():
 discount = total - 2000
 if month > 12:
  print(discount)
 else:
    print(total)
calculate()

# Start with a variable: total_requests = 0
# Ask: How many users logged in today?
# Add that to total_requests
# Ask: How many failed logins?
# Add that to total_requests
# Print: “Total server requests handled today: <value>”


logged_in = int(input("how many users logged in today? "))
requests = 0 + logged_in
log_failed = int(input("how many failed logins? "))
total_requests = requests + log_failed
print(f"Total server requests handled today: {total_requests}")

# Ask for age
# Ask for access code
# If age >= 18 AND code is "trace-vault-access"
# Print: "Access granted to Vault"
# Else print: "You are not permitted to access this feature"

age = int(input("How old are u? "))
access_code = str(input("Enter your access code: "))
if age >= 18 and access_code == "trace-vault":
    print("Access granted to Vault")
else:
    print("You are not permitted to access this feature")

# Ask user to enter ANYTHING
# Print out what they entered and its data type
# (use type() to reveal if it’s string, int, etc.)

anything = (input())
print(anything,   type(anything))


# Ask user: How can I help you? (choose from: login, signup, forgot password)
# If they type login → print: "Redirecting to login page..."
# If signup → "Creating a new account..."
# If forgot password → "Sending reset email..."
# If anything else → "Command not recognized"

want = str(input("How can I help you? (choose from: login, signup, forgot password): "))
if want == "login":
    print("Redirecting to login page...")
elif want == "signup":
    print("creating a new account..")
elif want == "forgot password":
    print("Sending reset email..")
else:
    print("request not recognized")
