# Exercise 1 — Age
# Create:
# age = 30

# If the age is 18 or above:
# Adult

# Otherwise:
# Minor

age = 30

if age >= 18:
    print("Adult")
else:
    print("Minor")

# Exercise 2 — Grade
# Create:
# marks = 75

# Use if, elif, and else.

# Rules:
# 80-100 → A+
# 70-79  → A
# 60-69  → B
# 50-59  → C
# 40-49  → D
# Below 40 → F

# Expected:
# A

marks = 75

if marks >= 80:
    print("A+")
elif marks >= 70:
    print("A")
elif marks >= 60:
    print("B")
elif marks >= 50:
    print("C")
elif marks >= 40:
    print("D")
else:
    print("F")

# Exercise 3 — Login
# Create:
# email = "admin@example.com"
# password = "123456"

# Check both email and password.

# If both are correct:
# Login successful

# Otherwise:
# Invalid credentials
# Use and

email = "admin@example.com"
password = "123456"

if email == "admin@example.com" and password == "123456":
    print("Login successful")
else:
    print("Invalid credentials")

# Exercise 4 — Agent verification
# Create:
# is_verified = True
# is_active = True

# The agent should only get access when both are true.

# Expected:
# Access granted

# Otherwise:
# Access denied

is_verified = True
is_active = True

if is_verified and is_active:
    print("Access granted")
else:
    print("Access denied")

# Exercise 5 — Backend-style logic 🚀
# Create:
# age = 25
# is_verified = True
# is_active = True
# is_admin = False

# Rules:
# User must be 18+
# User must be verified
# User must be active
# OR user can access if they are an admin

# Think carefully about the condition.

# Expected:
# Access granted
# Try to write the condition yourself rather than copying the examples above.

age = 25
is_verified = True
is_active = True
is_admin = False

if (age >= 18 and is_verified and is_active) or is_admin:
    print("Access granted")
else:
    print("Access denied")



