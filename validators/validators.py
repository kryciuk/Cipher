from typing import List


def get_valid_input(prompt: str, valid_options: List[str]):
    """
    A function that validates the answer provided by the user..

            Returns:
                    choice (str): Validated answer.
    """
    choice: str = input(prompt)
    while choice not in valid_options:
        choice = input(f"Invalid option\n{prompt}")
    return choice
