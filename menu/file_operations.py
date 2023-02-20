from validators import get_valid_input
from buffer import Buffer
from file_handler import FileHandler
from colorama import Fore
from buffer import Message


class FileOperationsMenu:
    FILE_OPERATIONS_MAIN_MENU = (
        Fore.LIGHTCYAN_EX + "1 - Load file to the buffer\n2 - Save buffer to a "
        "new file (or overwrite old)\n3 - Append buffer to an existing "
        "file\n4 - Return to main menu\n"
    )

    @staticmethod
    def file_operations_menu():
        choice = get_valid_input(
            FileOperationsMenu.FILE_OPERATIONS_MAIN_MENU, ["1", "2", "3", "4"]
        )
        match choice:
            case "1":
                if Buffer.buffer != {"data": []}:
                    answer = get_valid_input(
                        "Buffer is not empty. Data will be overwritten. Continue? yes/no\n",
                        ["yes", "no"],
                    ).lower()
                    if answer == "yes":
                        loading_from_file_to_buffer(get_file_name())
                elif Buffer.buffer == {"data": []}:
                    loading_from_file_to_buffer(get_file_name())
            case "2":
                file_name = get_file_name()
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


def loading_from_file(file_name):
    transformed_data = {}
    data = FileHandler.load_file(file_name)
    transformed_data["data"] = [Message.from_dct(entry) for entry in data.get("data")]
    return transformed_data


def loading_from_file_to_buffer(file_name):
    Buffer.buffer = loading_from_file(file_name)


def get_file_name():
    file_name = input("Enter the name of the .json file: ") + ".json"
    return file_name
