from validators import choice_int_checker
from buffer import Buffer
from file_handler import FileHandler
from colorama import Fore


class FileOperationsMenu:
    @staticmethod
    def file_operations_main_menu():
        print(
            Fore.LIGHTCYAN_EX + "1 - Load file to the buffer\n"
            "2 - Save buffer to a new file (or overwrite old)\n"
            "3 - Append buffer to an existing file"
        )

    @staticmethod
    def file_operations_menu():
        FileOperationsMenu.file_operations_main_menu()
        choice = input()
        choice = choice_int_checker(choice)
        match choice:
            case 1:
                if Buffer.buffer != {"data": []}:
                    print("Buffer is not empty. Data will be overwritten. Continue?")
                    answer = input("yes/no\n").lower()
                    match answer:
                        case "yes":
                            file_name = (
                                input("Enter the name of the .json file: ") + ".json"
                            )
                            data = FileHandler.load_file(file_name)
                            Buffer.buffer = data
                            return file_name
                        case "no":
                            pass
                        case _:
                            print("Incorrect choice")
            case 2:
                file_name = input("Enter the name of the .json file: ") + ".json"
                FileHandler.save_to_new(file_name, Buffer.buffer)
                Buffer.clear_buffer()
            case 3:
                pass
                # file_name = input("Enter the name of the .json file: ") + ".json"
                # existing_content = FileHandler.load_file(file_name)
                # new_content = existing_content["data"] + Buffer.buffer["data"]
                # FileHandler.append_to_existing(file_name, new_content)
            case _:
                print("Incorrect choice")
