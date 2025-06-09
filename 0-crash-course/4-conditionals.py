# Python uses indentation to define blocks of code, not curly braces or other symbols

temp = 28
if temp > 30:
    print("It's hot outside")
elif temp > 20:
    print("It's a nice day!")
else:
    print("It's cold outside")

# Checking multiple conditions with logical operators
age = 25
has_license = True

if age >= 18 and has_license:
    print("You can drive a car.")
elif age >= 18 and not has_license:
    print("You need to get a driver's license first.")
else:
    print("You are too young to drive.")

# Nested conditionals
score = 85

if score >= 60:
    print("You passed!")
    if score >= 90:
        print("You got an A")
    elif score >= 80:
        print("You got a B!")
    elif score >= 70:
        print("You got a C")
    else:
        print("You got a D")
else:
    print("You failed!")

# Using the "in" operator with conditionals
fruit = "apple"
if fruit in ["banana", "apple", "orange"]:
    print(f"{fruit} is in the list.")

# Ternary operator (one-line if-else)
age = 20
status = "adult" if age >= 18 else "minor"
print(f"Status: {status}")

# Comparing strings
password = "secret123"
if password == "secret123":
    print("Access granted")
else:
    print("Access denied")

# Chaining comparisons
x = 15
if 10 < x < 20:
    print("x is between 10 and 20")

# truthy or falsy
user_input = ""
if user_input:
    print("Input provided.")
else:
    print("No input provided")
