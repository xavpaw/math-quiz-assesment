math_list = ["addition", "subtraction", "multiplication"]

# question input
import random

def addition(num_1, num_2):
    return num_1 + num_2

def subtraction(num_1, num_2):
    return num_1 - num_2

def multiplication(num_1, num_2):
    return num_1 * num_2

# List of operations
operations = [addition, subtraction, multiplication]

# Choose a random operation
operation = random.choice(operations)

# difficulty math settings / number generator
if difficulty == "3":
    num_1 = random.randit(1, 55)
    num_2 = random.randit(1, 55)
elif difficulty == "2":
    num_1 = random.randit(1, 30)
    num_2 = random.randit(1, 30)
else:
    num_1 = random.randit(1, 15)
    num_2 = random.randit(1, 15)

# Perform the chosen operation
result = operation(x, y)

# Generate the question based on the operation
if operation == addition:
    question = f"What is {x} + {y}?"
elif operation == subtraction:
    question = f"What is {x} - {y}?"
elif operation == multiplication:
    question = f"What is {x} * {y}?"

# Print the question
print("Question:", question)