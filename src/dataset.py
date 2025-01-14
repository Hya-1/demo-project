# Basic Python Script

# Variables
message = "Hello, World!"
number = 42
pi = 3.14159

# Print variables
print(message)
print("Number:", number)
print("Pi:", pi)


# Function
def greet(name):
    return f"Hello, {name}!"


# Call function
print(greet("Alice"))

# Loop
for i in range(5):
    print(f"Loop iteration {i}")


# Class
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"


# Create an instance of the class
my_dog = Dog("Buddy", 3)

# Call method
print(my_dog.bark())
