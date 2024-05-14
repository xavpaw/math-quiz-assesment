print("Mathematics quiz")


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
    
In this quiz you will be asked a series of
mathematical equations and you can write
down your answers next to the question.

     ''')



# Main routine
print()
print("Mathematics quiz")
print()

# loop for testing purposes
want_instructions = yes_no("Do you want to read the instructions? ")

if want_instructions == "yes":
    instruction()

