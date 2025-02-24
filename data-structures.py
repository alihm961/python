# EXERCISE 1 LIST OPERATIONS

#  Create a List
numbers = [10, 20, 30, 40, 50]

# Add Elements
numbers.append(60)
# Insert 25 at index 2
numbers.insert(2, 25)

# Remove Elements
numbers.remove(40) # Remove by value
last = numbers.pop() # Remove last element

# Slicing
print("First 3 numbers:", numbers[:3])

# Sorting
numbers.sort()
print("Sorted List:", numbers)


# EXERCISE 2 Tuple & Set Operations

# Tuple (Immutable)
coordinates = (4, 5)
print("Tuples:", coordinates)

# Set (Unique values)
unique_numbers = {1, 2, 3, 4, 5}
unique_numbers.add(6)
unique_numbers.remove(2)
print("Set:", unique_numbers)


# EXERCISE 3 Dictionary Operations

# Dictionary (Key-Value Pairs)
student = {"name": "Nabiha", "age": 20, "grade": "A"}

# Update value
student["age"] = 21

# Add new key-value
student["City"] = "Beirut"

# Delete key
del student["grade"]

# Iterate through keys and values
for key, value in student.items():
    print(key, ":", value)


