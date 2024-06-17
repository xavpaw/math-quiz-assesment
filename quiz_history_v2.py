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

quiz_history = []

# Main routine
print()
print("Mathematics quiz")
print()

# loop for testing purposes
want_instructions = yes_no("Do you want to read the instructions? ")

if want_instructions == "yes":
    instruction()


# difficulty selection from Chat GPT
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


# Define operation functions
def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b



correct_answers = 0

while True:
    try:
        difficulty = int(input("Enter the difficulty level (1 / easy, 2 / medium, or 3 / hard): "))
        if difficulty in [1, 2, 3]:
            break
        else:
            print("Invalid input. Please enter a number between 1, 2, or 3.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

if difficulty == 3:
    max_num = 55
elif difficulty == 2:
    max_num = 30
else:
    max_num = 15

try:
    for _ in range(20):  # Assuming you have 20 questions
        num_1 = random.randint(1, max_num)
        num_2 = random.randint(1, max_num)

        # List of operations
        operations = [addition, subtraction, multiplication]

        # Choose a random operation
        operation = random.choice(operations)

        # Perform the chosen operation
        result = operation(num_1, num_2)

        # Ask the question and get user input from ChatGPT
        question = f"What is {num_1} {'+' if operation == addition else '-' if operation == subtraction else '*'} {num_2}? "
        while True:
            answer = input(question)
            if not answer.strip() or not answer.lstrip('-').isdigit():
                print("Please enter a valid number.")
            else:
                break

        # Convert the input to an integer
        answer = int(answer)

        # Check the answer
        if answer == result:
            feedback = "Correct!"
            correct_answers += 1
        else:
            feedback = "Incorrect!"

except ValueError:
    print("Please enter a valid number.")

# Display the final score

history_feedback = f"Question {num_1}: {feedback}"
quiz_history.append(history_feedback)

# Ask user if they want to see their game history and output it if requested.
see_history = input("\nDo you want to see your game history? (yes/no): ")

# Check if input is empty
if see_history.strip() == "":
    print("Please enter yes or no")
elif see_history.lower() == "yes":
    if quiz_history:
        for item in quiz_history:
            print(item)

else:
    print("Oops - you chickened out!")

print("\nThanks for playing")


