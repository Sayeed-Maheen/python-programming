# Collections
# 1. List
# 2. Dictionary
# 3. Tuple
# 4. Set
# 5. Nested data
# 6. List of dictionaries ← very important for APIs

# List
names = ["Sayeed", "Rahim", "Karim"] # This creates a list with three items
print(names)
print(names[0])
print(names[1])
print(names[2])
print(names[-1])
print(names[-2])

names[1] = "Hassan" # This changes the item at index 1 to "Hassan"
print(names)

names.append("Rahim") # This adds "Rahim" to the end of the list
print(names)
# names.append(["Abdullah", "Habib"]) # This adds the list as a single item
print(names)

names.extend(["Maheen", "Rofiq"]) # This adds the items to the end of the list
print(names)

names.remove("Rahim") # This removes the first occurrence of "Rahim"
print(names)

names.pop(2) # This removes the item at index 2
print(names)
names.pop() # This removes the last item.
print(names)

print(len(names)) # This returns the number of items in the list

if "Maheen" in names: # This checks if "Maheen" is in the list
       print("User found")
else:
    print("User not found")

if "Karim" not in names: # This checks if "Karim" is not in the list
    print("User not found")
else:
    print("User found")

for name in names: # This loopsates through each item in the list
     print(name)

# List slicing ⭐
numbers = [10, 20, 30, 40, 50] # This creates a list with five items
print(numbers[0:3]) # This slices the list from index 0 to 2

numbers = [10, 20, 30, 40, 50]

print(numbers[:3]) # This slices the list from index 0 to 2
print(numbers[2:]) # This slices the list from index 2 to the end
print(numbers[1:4]) # This slices the list from index 1 to 3
print(numbers[-2:]) # This slices the list from the second last item to the end

# Dictionary
user = { 
    "id": 1,
    "name": "Sayeed",
    "email": "sayeed@example.com",
    "is_active": True
}  # This creates a dictionary with four items

print(user) # This prints the dictionary
print(user["id"]) # This prints the value of the item with the key "id"

user["phone"] = "01759863102" # This adds a new item with the key "phone" and the value "01759863102"
print(user)

user["name"] = "Sayeed Hassan" # This changes the value of the item with the key "name" to "Sayeed Hassan"
print(user)

del user["phone"] # This deletes the item with the key "phone"
print(user)

# get() ⭐
print (user.get("email" , "No email found")) # This returns the value of the item with the key "email" if it exists, otherwise it returns the value of the second argument
if user.get("email") is None: # This checks if the item with the key "email" exists
    print("No email found") # This prints "No email found" if the item with the key "email" does not exist
else:
    print(user["email"]) # This prints the value of the item with the key "email"

# Another example
if "email" in user:
    print(user["email"])
else:
    print("Email not available")

# Dictionary keys and values
print(user.keys()) # This prints the keys of the dictionary
print(user.values()) # This prints the values of the dictionary
print(user.items()) # This prints the items of the dictionary (key-value pairs)

# Loop through a dictionary
user = {
    "id": 1,
    "name": "Sayeed",
    "email": "sayeed@example.com"
} 

for key, value in user.items(): # This loops through each item in the dictionary 
    print(f"{key}: {value}")

# Nested dictionaries
user = {
    "id" : 1,
    "name" : "Sayeed Hassan",
    "contact" : { 
        "phone" : "01759863102", 
        "email" : "sayeedhassan1124@gmail.com"
    }
}
print(user) # This prints the dictionary
print(user["name"]) # This prints the value of the item with the key "name"
print(user["contact"]["phone"]) # This prints the value of the item with the key "phone" in the nested dictionary

# List + Dictionary ⭐⭐⭐
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
    }
]
print(users);
print(users[0]["name"]);
print(users[1]["email"]);


