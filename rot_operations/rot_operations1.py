from menu.menu import Menu
from file_handler.file_handler import FileOperations


# def user_permission_checker(func):
#     def wrapper(*args, **kwargs):
#         if args[0].author_id == args[1].author_id:
#             return func(*args, **kwargs)
#         return "Denied"
#     return wrapper


class RotOperations:
    @staticmethod
    def encoding():
        Menu.rot_choice()
        choice = int(input())
        match choice:
            case 1:
                return RotOperations.encoding_rot13()
            case 2:
                return RotOperations.encoding_rot47()
            case _:
                print("Incorrect choice")

    @staticmethod
    def decoding():
        Menu.rot_choice()
        choice = int(input())
        match choice:
            case 1:
                return RotOperations.decoding_rot13()
            case 2:
                return RotOperations.decoding_rot47()
            case _:
                print("Incorrect choice")

    @staticmethod
    def encoding_rot13():
        file_to_encrypt = input("Enter the name of the file that will be encrypted.\n")
        Menu.file_choice()
        choice = int(input())
        if choice == 2:
            new_file_name = input("Enter the file name...\n")
        match choice:
            case 1:
                FileOperations.encrypt_add_rot13(file_to_encrypt)
            case 2:
                FileOperations.encrypt_create_rot13(file_to_encrypt, new_file_name)
            case _:
                print("Incorrect choice")

    @staticmethod
    def encoding_rot47():
        file_to_encrypt = input("Enter the name of the file that will be encrypted.\n")
        Menu.file_choice()
        choice = int(input())
        if choice == 2:
            new_file_name = input("Enter the file name...\n")
        match choice:
            case 1:
                FileOperations.encrypt_add_rot47(file_to_encrypt)
            case 2:
                FileOperations.encrypt_create_rot47(file_to_encrypt, new_file_name)
            case _:
                print("Incorrect choice")

    @staticmethod
    def decoding_rot13():
        file_to_decrypt = input("Enter the name of the file that will be decrypted.\n")
        Menu.file_choice()
        choice = int(input())
        if choice == 2:
            new_file_name = input("Enter the file name...\n")
        match choice:
            case 1:
                FileOperations.decrypt_add_rot13(file_to_decrypt)
            case 2:
                FileOperations.decrypt_create_rot13(file_to_decrypt, new_file_name)
            case _:
                print("Incorrect choice")

    @staticmethod
    def decoding_rot47():
        file_to_decrypt = input("Enter the name of the file that will be decrypted.\n")
        Menu.file_choice()
        choice = int(input())
        if choice == 2:
            new_file_name = input("Enter the file name...\n")
        match choice:
            case 1:
                FileOperations.encrypt_add_rot47(file_to_decrypt)
            case 2:
                FileOperations.encrypt_create_rot47(file_to_decrypt, new_file_name)
            case _:
                print("Incorrect choice")
