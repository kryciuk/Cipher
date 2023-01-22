from functionality.rot import Rot47, Rot13


class Manager:
    def start(self):
        self.show_menu()
        self.execute()

    @staticmethod
    def show_menu():
        Menu.show_menu()

    @staticmethod
    def execute():
        choice = int(input())
        match choice:
            case 1:
                return Manager.encoding()
            case 2:
                return Manager.decoding()
            case 3:
                exit()
            case _:
                print("Incorrect choice")

    @staticmethod
    def encoding():
        Menu.rot_choice()
        choice = int(input())
        match choice:
            case 1:
                return Manager.encoding_rot13()
            case 2:
                return Manager.encoding_rot47()
            case _:
                print("Incorrect choice")

    @staticmethod
    def decoding():
        Menu.rot_choice()
        choice = int(input())
        match choice:
            case 1:
                return Manager.decoding_rot13()
            case 2:
                return Manager.decoding_rot47()
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


class FileOperations:
    @classmethod
    def encrypt_add_rot13(cls, file_name):
        with open(file_name, "a+") as file:
            file.seek(0)
            lines = file.read()
            lines_encoded = Rot13.encode(lines)
            file.write(lines_encoded)

    @classmethod
    def encrypt_create_rot13(cls, file_name, new_file_name):
        with open(file_name, "r") as file:
            lines = file.read()
        with open(new_file_name, "w") as file:
            file.write(Rot13.encode(lines))

    @classmethod
    def encrypt_add_rot47(cls, file_name):
        with open(file_name, "a+") as file:
            file.seek(0)
            lines = file.read()
            lines_encoded = Rot47.encode(lines)
            file.write(lines_encoded)

    @classmethod
    def encrypt_create_rot47(cls, file_name, new_file_name):
        with open(file_name, "r") as file:
            lines = file.read()
        with open(new_file_name, "w") as file:
            file.write(Rot47.encode(lines))

    @classmethod
    def decrypt_add_rot13(cls, file_name):
        with open(file_name, "a+") as file:
            file.seek(0)
            lines = file.read()
            lines_decoded = Rot13.decode(lines)
            file.write(lines_decoded)

    @classmethod
    def decrypt_create_rot13(cls, file_name, new_file_name):
        with open(file_name, "r") as file:
            lines = file.read()
        with open(new_file_name, "w") as file:
            file.write(Rot13.decode(lines))

    @classmethod
    def decrypt_add_rot47(cls, file_name):
        with open(file_name, "a+") as file:
            file.seek(0)
            lines = file.read()
            lines_decoded = Rot47.decode(lines)
            file.write(lines_decoded)

    @classmethod
    def decrypt_create_rot47(cls, file_name, new_file_name):
        with open(file_name, "r") as file:
            lines = file.read()
        with open(new_file_name, "w") as file:
            file.write(Rot47.decode(lines))


class Menu:
    @staticmethod
    def show_menu():
        print(
            "What do you want to do?\n1 - encode file\n2 - decode file\n3 - end program"
        )

    @staticmethod
    def get_choice():
        return int(input())

    @staticmethod
    def rot_choice():
        print(
            "Enter the number corresponding to the cipher you want to use:\n1 - Rot13\n2 - Rot47"
        )

    @staticmethod
    def file_choice():
        print(
            "Add the encoded message to an existing file or create a new one?\n1 - Add\n2 - Create new"
        )


class Buffer:
    def __init__(self):
        self.storage_rot13_encoded = []
        self.storage_rot47_encoded = []
        self.storage_rot13_decoded = []
        self.storage_rot47_decoded = []

    def add(self):
        pass


def main():
    manager = Manager()
    manager.start()


if __name__ == "__main__":
    main()