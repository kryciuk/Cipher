from validators import get_valid_input
from buffer import Buffer
from file_handler import FileHandler
from colorama import Fore
from buffer import Message
from typing import Dict, List, Any


class FileOperationsMenu:
    """
    A class representing a menu with file operations possible in the program.
    ...

    Attributes
    ----------
    FILE_OPERATIONS_MAIN_MENU : str
        Shows the possible options to choose from the menu.

    Methods
    ----------
    file_operations_menu
        A method that displays the menu and gets the response from the user.
    loading_from_file
        A method that converts data retrieved from a file into a dictionary containing Message objects.
    loading_from_file_to_buffer
        A method that converts the data retrieved from the file into a
        dictionary containing Message objects and loads them into the buffer.
    get_file_name
        A method that gets the file name from the user.

    """

    FILE_OPERATIONS_MAIN_MENU: str = (
        Fore.LIGHTCYAN_EX + "1 - Load file to the buffer\n2 - Save buffer to a "
        "new file (or overwrite old)\n3 - Append buffer to an existing "
        "file\n4 - Return to main menu\n"
    )

    @staticmethod
    def file_operations_menu() -> None:
        """
        A method that displays the menu and gets the response from the user.

        """
        choice: str = get_valid_input(
            FileOperationsMenu.FILE_OPERATIONS_MAIN_MENU, ["1", "2", "3", "4"]
        )
        match choice:
            case "1":
                if Buffer.buffer != {"data": []}:
                    answer: str = get_valid_input(
                        "Buffer is not empty. Data will be overwritten. Continue? yes/no\n",
                        ["yes", "no"],
                    ).lower()
                    if answer == "yes":
                        loading_from_file_to_buffer(get_file_name())
                elif Buffer.buffer == {"data": []}:
                    loading_from_file_to_buffer(get_file_name())
            case "2":
                file_name: str = get_file_name()
                FileHandler.save(file_name, Buffer.transform_to_dict())
                Buffer.clear_buffer()
            case "3":
                file_name = get_file_name()
                existing_data = loading_from_file(file_name)
                Buffer.buffer = {"data": existing_data["data"] + Buffer.buffer["data"]}
                FileHandler.save(file_name, Buffer.transform_to_dict())
                Buffer.clear_buffer()
            case "4":
                return


def loading_from_file(file_name: str) -> Dict[str, List[Message]]:
    """
    A method that converts data retrieved from a file into a dictionary containing Message objects.

        Parameters:
                file_name (str): The name of the file to be loaded.

        Returns:
                transformed_data (Dict): A dictionary containing Message objects.
    """
    transformed_data: Dict[str, List[Message]] = {}
    data: Any = FileHandler.load(file_name)
    transformed_data["data"] = [Message.from_dct(entry) for entry in data.get("data")]
    return transformed_data


def loading_from_file_to_buffer(file_name: str) -> None:
    """
    A method that converts the data retrieved from the file into a dictionary containing Message objects and loads them into the buffer.

        Parameters:
                file_name (str): The name of the file to be loaded.

    """
    Buffer.buffer = loading_from_file(file_name)


def get_file_name() -> str:
    """
    A method that gets the file name from the user.

        Returns:
            file_name (str): The filename provided by the user.

    """
    file_name: str = input("Enter the name of the .json file: ") + ".json"
    return file_name
