# Print "Hello World!"
print("HEllo World!")

# Variables and Data Types
name = "Alice"
age = 25
height = 5.6
is_student = True

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Student:", is_student)

# User Input
user_name = input("Enter your name: ")
print("Welcome,", user_name)

# Basic Arithmetic Operations
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
print("Quotient:", num1 / num2)

# If-Else Conditions
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
    
# Loops 
for i in range(1, 6):
    print(i)
    
# Function
def square(n):
    return n * n
print("Square of 4:", square(4))