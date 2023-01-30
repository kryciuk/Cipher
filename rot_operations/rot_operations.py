from menu.menu import Menu
from file_handler.file_handler import FileHandler


class RotOperations:
    @staticmethod
    def encoding_decoding():
        Menu.rot_choice()
        rot_choice = int(input())
        file_to_encrypt = input("Enter the name of the file that will be encrypted.\n")
        Menu.file_choice()
        file_choice = int(input())
        if file_choice == 2:
            new_file_name = input("Enter the file name...\n")
        match [rot_choice, file_choice]:
            case [1, 1]:
                return FileHandler.encrypt(file_choice, file_to_encrypt, rot_choice)
            case [1, 2]:
                return FileHandler.encrypt(
                    file_choice, file_to_encrypt, rot_choice, new_file_name
                )
            case [2, 1]:
                return FileHandler.decrypt(file_choice, file_to_encrypt, rot_choice)
            case [2, 2]:
                return FileHandler.decrypt(
                    file_choice, file_to_encrypt, rot_choice, new_file_name
                )
            case _:
                print("Incorrect choice")
