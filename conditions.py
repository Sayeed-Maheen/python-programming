# Conditions
# if, elif, else

# if statement
age = 30
is_active = True

if age >= 18:
    print("Adult")

# if else statement
age = 16

if age >= 18:
    print("Adult")    
else:
    print("Child")

# elif statement (else if)
age = 16

if age >= 18:
    print("Adult")    
elif age >= 13:
    print("Teenager")
else:
    print("Child")

# Comparison operators
# ==, !=, >, <, >=, <=
email = "sayeedhassan@gmail.com"
password = "123456"

if email == "user@example.com" and password == "123456":
    print("Login successful")
else:
    print("Invalid email or password")

# and operator
# Returns True if both conditions are True
# Returns False if any condition is False
if age >= 18 and is_active:
    print("Adult and active")
else:
    print("Not an adult or inactive active")

# or operator
# Returns True if any condition is True
# Returns False if both conditions are False
if age >= 18 or is_active:
    print("Adult or active")
else:
    print("Not an adult or inactive active")

# not operator
# Returns True if the condition is False
# Returns False if the condition is True
if not is_active:
    print("Inactive")
else:
    print("Active")

# Combining conditions
age = 25
is_verified = True
is_active = True

if age >= 18 and is_verified and is_active:
    print("User can access the system")
else:
    print("Access denied")

# Nested if statements
is_logged_in = True
is_verified = True

if is_logged_in:
    if is_verified:
        print("Welcome")
    else:
        print("Please verify your account")
else:
    print("Please login")

# Python's truthiness
# True, False, None, empty strings, empty lists, empty tuples, empty sets, empty dictionaries, 0, -0, NaN, and -inf are all False
# All other values are True

name = ""

if name:
    print("Name exists")
else:
    print("Name is empty")


items = ["Banana", "Apple", "Orange", "Mango"]

if items:
    print("Items available")
else:
    print("No items")
    

users = []

if users:
    print("Users found")
else:
    print("No users found")
