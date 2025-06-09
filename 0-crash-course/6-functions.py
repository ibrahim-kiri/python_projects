# Functions are blocks of code that can be reused, they can take arguments and return values
# 

def greet_user(name):
    print(f"Hello,", name, "Welcome to our app")
    print("We hope you enjoy using our services.")
    print("Let us know if you need any help.")

greet_user("Alice")
greet_user("Bob")
greet_user("Charlie")

def power(base, exponent):
    return base ** exponent

x = power(2, 5) #32
y = power(8, 2) #64
z = power(3, 3) #27

print("x:", x)
print("y:", y)
print("z:", z)