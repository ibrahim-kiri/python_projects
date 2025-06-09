import math

# Basic operations in Python
x = 10
y = 5

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)
print(x**y)

# x = x + 15
x += 15
print(x)

# String concatenation
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)

print("Hey my name is " + first_name + " and my last name is " + last_name)

# f strings
print(f"Hey my name is {first_name} and my last name is {last_name}")

# Int floor division
a = 17
b = 5
print(a / b)
print(a // b)  # Floor division

# Assign multiple variables
i, j, k = 1, 2, 3
print(i, j, k)

# Swap values
m = 10
n = 20
m, n = n, m
print(m, n)

# Comparison operations
c = 5
d = 10
print(c == d)
print(c != d)
print(c > d)
print(c < d)
print(c >= d)
print(c <= d)

# Logical operators
a = True
b = False  

print(a and b)
print(a or b)
print(not b)

# String slicing
text = "Python programming"
print(text[0:6])
print(text[7:])
print(text[::-1])

# String formatting with .format()
name = "Alice"
age = 25
msg = "My name is {} and I am {} years old".format(name, age)
print(msg)

# Using placeholders
msg2 = "My name is {0} and I am {1} years old. {0} is a nice name".format(name, age)
print(msg2)

# Math module operations
print(math.pi)
print(math.sqrt(16))
print(math.floor(4.7)) #4.0
print(math.ceil(5.3))  #6.0
print(math.pow(2, 3))  # 8.0

pi = 3.141592653589793
print(round(pi, 2))  # Rounding to 2 decimal places
