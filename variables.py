# Checking a variable's type
# type()
name = "Sayeed"
age = 25
salary = 50000.50
is_active = True

print(type(name))
print(type(age))
print(type(salary))
print(type(is_active))

# Changing variables. Variables can be changed.
name = "Sayeed"
print(name)

name = "Maheen"
print(name)

# Python is dynamically typed. But it is a bad practice. Keeping variables predictable makes code much easier to understand
value = 10
value = "Hello"
value = True

# Basic arithmetic
a = 10
b = 5

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)   # Floor division operator returns the quotient of the division
print(a % b)    # Modulus operator returns the remainder of the division
print(a ** b)   # Exponent operator returns the result of a to the power of b

# Even and odd numbers
num = 11
if num % 2 == 0:
    print ("This number is even.")
else:
    print ("This number is odd.")

# String concatenation
name = "Maheen"
age = 30
print("My name is " + name + " and I am " + str(age) + " years old.")

# String formatting (f-strings)⭐ Similar to Dart string interpolation (print("My name is $name");)
name = "Maheen"
age = 30
print(f"My name is {name} and I am {age} years old.")