# Exercise 1 — Variables
''' 
Create these variables:
name
age
email
phone
is_developer

Give them appropriate values. Then print all of them. 
'''

name = "Sayeed"
age = 30
email = "sayeedhassan1124@gmail.com"
phone = "01759863102"
is_developer = True

print(name)
print(age)
print(email)
print(phone)
print(is_developer)


# Exercise 2 — User information
'''
Create:
name = "Sayeed"
age = 25
profession = "Flutter Developer"

Print:
My name is Sayeed.
I am 25 years old.
I am a Flutter Developer.

Try using an f-string.
'''

name = "Sayeed"
age = 25
profession = "Flutter Developer"

print(f"My name is {name}")
print(f"I am {age} years old.")
print(f"I am a {profession}.")

# Exercise 3 — Calculator
'''
Create:
a = 20
b = 5

Print:
Addition
Subtraction
Multiplication
Division

For example:
Addition: 25
Subtraction: 15
Multiplication: 100
Division: 4.0
'''

a = 20
b = 5

addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b

print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")

# Exercise 4 — Types
'''
Create:
name = "Sayeed"
age = 25
salary = 50000.50
is_active = True

Print the type of each variable using:
type()
'''

name = "Sayeed"
age = 25
salary = 50000.50
is_active = True

print(type(name))
print(type(age))
print(type(salary))
print(type(is_active))

# Exercise 5 — Backend thinking 🚀
'''
Imagine you're storing an agent's information.

Create:
agent_id
name
email
phone
commission
is_verified

Give them realistic values and print them using an f-string.

For example, your output should look roughly like:
Agent ID: 101
Name: Sayeed
Email: ...
Phone: ...
Commission: ...
Verified: True

This is intentionally preparing you for the kind of data you'll eventually handle in Django APIs.
'''

agent_id = 1
name = "Sayeed Hassan"
email = "sayeedhassan1124@gmail.com"
phone = "01759863102"
commission = 10000.00
is_verified = True

print(f"Agent ID: {agent_id}")
print(f"Name: {name}")
print(f"Email: {email}")
print(f"Phone: {phone}")
print(f"Commission: {commission}")
print(f"Verified: {is_verified}")
