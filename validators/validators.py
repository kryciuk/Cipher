def get_valid_number_input(
    prompt,
):
    user_instruction = input(prompt)
    try:
        user_instruction = int(user_instruction)
    except ValueError:
        print("Invalid input. Please enter a number")
        return get_valid_number_input(prompt)

    return user_instruction


def get_valid_input(prompt, valid_options: list = None):
    choice = input(prompt)
    while choice not in valid_options:
        choice = input(f"Invalid option\n{prompt}")
    return choice
