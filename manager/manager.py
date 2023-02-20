from menu import Menu, BufferMenu, FileOperationsMenu
from functionality import get_rot
from colorama import Fore
from buffer import Message, Buffer
from validators import get_valid_input


class Manager:
    def __init__(self):
        self.rot = get_rot("rot13")

    def start(self):
        while True:
            self.show_menu()
            self.execute()

    def show_menu(self):
        print(Fore.LIGHTYELLOW_EX + f"SELECTED ROT TYPE: {self.rot.__name__} ")

    def execute(self):
        choice = get_valid_input(Menu.main_menu, ["1", "2", "3", "4", "5", "6"])
        match choice:
            case "1":
                self.change_rot()
            case "2":
                self.encode_decode(status="encoded")
            case "3":
                self.encode_decode(status="decoded")
            case "4":
                BufferMenu.buffer_menu()
            case "5":
                FileOperationsMenu.file_operations_menu()
            case "6":
                exit()

    def change_rot(self):
        rot = get_valid_input("Set ROT: rot13/rot47: ", ["rot13", "rot47"]).lower()
        self.rot = get_rot(rot)

    def encode_decode(self, status):
        message = input("Write a message: ")
        modified_message = Message(
            self.rot.__name__, self.rot.encode_decode(message), status
        )
        Buffer.add_message_to_buffer(modified_message)
