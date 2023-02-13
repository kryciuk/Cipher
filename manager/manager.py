from menu import Menu, BufferMenu, FileOperationsMenu
from functionality import get_rot
from colorama import Fore
from buffer import Message, Buffer
from validators import choice_int_checker


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
        choice = input()
        choice = choice_int_checker(choice)
        match choice:
            case 1:
                self.change_rot()
            case 2:
                self.encode()
            case 3:
                self.decode()
            case 4:
                BufferMenu.buffer_menu()
            case 5:
                FileOperationsMenu.file_operations_menu()
            case 6:
                exit()
            case _:
                print("Incorrect choice")

    def change_rot(self):
        print("Set ROT: rot13/rot47")
        rot = ""
        while rot not in ["rot13", "rot47"]:
            rot = input("Pick rot: ").lower()
        self.rot = get_rot(rot)

    def encode(self):
        message = input("Write a message: ")
        modified_message = Message(
            self.rot.__name__, self.rot.encode(message), "encoded"
        )
        Buffer.buffer["data"].append(modified_message.to_dct())

    def decode(self):
        message = input("Write a message: ")
        modified_message = Message(
            self.rot.__name__, self.rot.decode(message), "decoded"
        )
        Buffer.buffer["data"].append(modified_message.to_dct())
