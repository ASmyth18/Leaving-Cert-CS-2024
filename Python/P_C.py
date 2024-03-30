# Variables and Data Types
x = 5
y = "Hello, World!"

# Control Flow
if x > 0:
    print("Positive")
else:
    print("Zero or Negative")

# Functions
def greet(name):
    print(f"Hello, {name}!")

# Lists
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers)

# Dictionaries
person = {"name": "John", "age": 25}
person["city"] = "New York"
print(person)

# Sets
fruits = {"apple", "banana", "orange"}
fruits.add("grape")
print(fruits)

# Tuples
coordinates = (10, 20)
print(coordinates)

# File Handling
with open("file.txt", "w") as file:
    file.write("Hello, World!")

with open("file.txt", "r") as file:
    content = file.read()
    print(content)

# Exception Handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero!")

# Classes and Objects
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

rect = Rectangle(5, 3)
print(rect.area())

# Function Call
greet("Alice")