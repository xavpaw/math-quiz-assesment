# checks users enter yes (y) or no (n)
def yes_no(question):
    while True:
        response = input(question).lower()

        # checks user response, question
        # repeats if user don't doesn't yes/no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes / no")


# Displays instructions to user
def instruction():
    print('''

In this mathematical quiz you will be
asked 20 random questions that can either
be subtraction, multiplication or addition.

put down your answers next to
the question.

     ''')


# Main routine
print()
print("Mathematics quiz")
print()

# loop for testing purposes
want_instructions = yes_no("Do you want to read the instructions? ")

if want_instructions == "yes":
    instruction()

# difficulty selection
def int_check(prompt, low, high):
    """
    Prompt the user to input an integer within a specified range.

    Args:
    prompt (str): The message to display to the user.
    low (int): The minimum acceptable integer.
    high (int): The maximum acceptable integer.

    Returns:
    int: The valid integer input by the user within the specified range.
    """
    while True:
        try:
            value = int(input(prompt))
            if low <= value <= high:
                return value
            else:
                print(f"Please enter a number between {low} and {high}.")
        except ValueError:
            print("Please enter a valid integer.")

# random equation generator
import random

# Define operations
def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

# Store correct answers
correct_answers = 0

# difficullty
# Example usage
difficulty = int_check("Select difficulty (level 1 / easy, level 2 / medium, level 3 / hard): ", low=1, high=3)
print(f"You selected difficulty level {difficulty}.")

# Generate and ask 20 questions
for _ in range(20):

    if difficulty == "3":
        num_1 = random.randint(1, 55)
        num_2 = random.randint(1, 55)
    elif difficulty == "2":
        num_1 = random.randint(1, 30)
        num_2 = random.randint(1, 30)
    else:
        num_1 = random.randint(1, 15)
        num_2 = random.randint(1, 15)

    # List of operations
    operations = [addition, subtraction, multiplication]

# Choose a random operation
    operation = random.choice(operations)

    # Perform the chosen operation
    result = operation(num_1, num_2)

# Choose a random operation
    if operation == addition:
        question = f"{num_1} + {num_2} = "
    elif operation == subtraction:
        question = f"{num_1} - {num_2} = "
    elif operation == multiplication:
        question = f"{num_1} * {num_2} = "

    # Ask the question and get user input
    answer = input(question)

    # Check if the answer is correct
    if int(answer) == result:
        print("Correct!")
        correct_answers += 1
    else:
        print("Incorrect!")

# Display the final score
print(f"You got {correct_answers} out of 20 questions correct.")