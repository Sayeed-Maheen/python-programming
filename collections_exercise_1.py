# Exercise 1 — List basics

# Create:
# fruits = ["Apple", "Banana", "Mango", "Orange"]

# Do the following:
# Print the first fruit.
# Print the last fruit.
# Add "Grapes".
# Remove "Banana".
# Print the length.
# Check whether "Mango" exists.

fruits = ["Apple", "Banana", "Mango", "Orange"]
print(fruits[0])
print(fruits[-1])
fruits.append("Grapes")
print(fruits)
fruits.remove("Banana")
print(fruits)
print(len(fruits))
if("Mango" in fruits):
    print("Mango exists")
else:
    print("Mango does not exist")


# Exercise 2 — Numbers

# Create:
# numbers = [10, 20, 30, 40, 50]

# Print:
# First number
# Last number
# First 3 numbers
# Last 2 numbers

# Use indexing and slicing.

numbers = [10, 20, 30, 40, 50]
print(numbers[0])
print(numbers[-1])
print(numbers[:3])
print(numbers[-2:])


# Exercise 3 — User dictionary

# Create:
# user = {
#     "id": 1,
#     "name": "Sayeed",
#     "email": "sayeed@example.com",
#     "phone": "01759863102",
#     "is_verified": True
# }

# Then:
# Print the name.
# Print the email.
# Change the phone number.
# Add "role": "admin".
# Print the role.
# Use get() to retrieve "address" with a default value "Not provided".

user = {
    "id": 1,
    "name": "Sayeed",
    "email": "sayeed@example.com",
    "phone": "01759863102",
    "is_verified": True
}
print(user["name"])
print(user["email"])
user["phone"] = "01753904301"
user["role"] = "admin"
print(user["role"])
print(user.get("address", "Not provided"))


# Exercise 4 — Users ⭐

# Create:
# users = [
#     {
#         "id": 1,
#         "name": "Sayeed",
#         "email": "sayeed@example.com"
#     },
#     {
#         "id": 2,
#         "name": "Rahim",
#         "email": "rahim@example.com"
#     },
#     {
#         "id": 3,
#         "name": "Karim",
#         "email": "karim@example.com"
#     }
# ]

# Use a for loop and print:
# 1 - Sayeed - sayeed@example.com
# 2 - Rahim - rahim@example.com
# 3 - Karim - karim@example.com

users = [
    {
        "id": 1,
        "name": "Sayeed",
        "email": "sayeed@example.com"
    },
    {
        "id": 2,
        "name": "Rahim",
        "email": "rahim@example.com"
    },
    {
        "id": 3,
        "name": "Karim",
        "email": "karim@example.com"
    }
]

for user in users:
    print(f"{user['id']} - {user['name']} - {user['email']}")


# Exercise 5 — API response ⭐⭐⭐

# Create:
# response = {
#     "status": "success",
#     "message": "Users fetched successfully",
#     "data": [
#         {
#             "id": 1,
#             "name": "Sayeed",
#             "email": "sayeed@example.com"
#         },
#         {
#             "id": 2,
#             "name": "Rahim",
#             "email": "rahim@example.com"
#         }
#     ]
# }

# Then:
# Print the status.
# Print the message.
# Print the first user's name.
# Print the second user's email.
# Use a loop to print all users.

# The final output should roughly be:
# Status: success
# Message: Users fetched successfully
# First User: Sayeed
# Second User Email: rahim@example.com

# 1 - Sayeed - sayeed@example.com
# 2 - Rahim - rahim@example.com

response = {
    "status": "success",
    "message": "Users fetched successfully",
    "data": [
        {
            "id": 1,
            "name": "Sayeed",
            "email": "sayeed@example.com"
        },
        {
            "id": 2,
            "name": "Rahim",
            "email": "rahim@example.com"
        }
    ]
}

print(response["status"])
print(response["message"])
print(response["data"][0]["name"])
print(response["data"][1]["email"])
for user in response["data"]:
    print(f"{user['id']} - {user['name']} - {user['email']}")


# One challenge for you 🚀

# Try this without looking back:
# users = [
#     {
#         "id": 1,
#         "name": "Sayeed",
#         "is_active": True
#     },
#     {
#         "id": 2,
#         "name": "Rahim",
#         "is_active": False
#     },
#     {
#         "id": 3,
#         "name": "Karim",
#         "is_active": True
#     }
# ]

# Print only active users.

# Expected:
# Sayeed
# Karim

users = [
    {
        "id": 1,
        "name": "Sayeed",
        "is_active": True
    },
    {
        "id": 2,
        "name": "Rahim",
        "is_active": False
    },
    {
        "id": 3,
        "name": "Karim",
        "is_active": True
    }
]

for user in users:
    if user["is_active"] == True:
        print(user["name"])
