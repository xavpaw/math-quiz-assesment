def intcheck(prompt, low, high):
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

# Example usage
difficulty = intcheck("Select difficulty (level 1 / easy, level 2 / medium, level 3 / hard): ", low=1, high=3)
print(f"You selected difficulty level {difficulty}.")

