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
