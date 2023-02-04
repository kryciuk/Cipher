from menu import Menu
from functionality import get_rot
from colorama import Fore
from file_handler.file_handler import FileHandler


class Manager:
    def __init__(self):
        self.rot = get_rot("rot13")

    def start(self):
        while True:
            self.show_menu()
            self.execute()

    def show_menu(self):
        print(Fore.LIGHTYELLOW_EX + f"SELECTED ROT TYPE: {self.rot.__name__} ")
        Menu.main_menu()

    def execute(self):
        choice = int(input())
        match choice:
            case 1:
                self.change_rot()
            case 2:
                self.write_or_load("encode")
                pass
            case 3:
                self.write_or_load("decode")
            case 4:
                # buffer
                pass
            case 5:
                # zakończ
                exit()
            case _:
                print("Incorrect choice")

    def change_rot(self):
        print("Set ROT: rot13/rot47")
        rot = ""
        while rot not in ["rot13", "rot47"]:
            rot = input("Pick rot: ").lower()
        self.rot = get_rot(rot)

    def write_or_load(self, method):
        Menu.write_load_menu()
        choice = int(input())
        match choice:
            case 1:
                message = input("Write a message: ")
                file_name = None
            case 2:
                file_name = input("Enter the name of the .json file: ") + ".json"
                message = FileHandler.load_message(file_name)
            case _:
                print("Incorrect choice")
        self.save_or_buffer(method, message, file_name)

    def save_or_buffer(self, method, message, file_name=None):
        if method == "encode":
            modified_message = self.rot.encode(message)
        elif method == "decode":
            modified_message = self.rot.decode(message)
        print(Fore.LIGHTYELLOW_EX, f"Your message: {modified_message}", sep="")
        Menu.save_or_buffer_menu()
        choice = int(input())
        match choice:
            case 1:
                self.new_or_existing(modified_message, file_name)
            case 2:
                # do buffera
                pass
            case 3:
                return None

    @staticmethod
    def new_or_existing(modified_message, file_name=None):
        if file_name is None:
            print(
                "The message was not loaded from a file. Only writing to a new file possible."
            )
            choice = 1
        elif file_name is not None:
            Menu.new_or_existing_menu()
            choice = int(input())
        match choice:
            case 1:
                new_file_name = input("Enter a file name: ") + ".json"
                return FileHandler.save_to_new(new_file_name, modified_message)
            case 2:
                pass
