from menu import Menu, BufferMenu, FileOperationsMenu
from functionality import get_rot
from colorama import Fore
from buffer import Message, Buffer
from validators import get_valid_input


class Manager:
    """
    A class that manages the main functions of the program.
    ...
    Attributes
    ----------
    rot : str
        The name of selected cipher.

    Methods
    ----------
    start
        Program launcher.
    execute
        Executes the program.
    change_rot
        A method for changing the cipher.
    encode_decode
        A method used to encode and decode messages.
    """

    def __init__(self):
        self.rot = get_rot("rot13")

    def start(self) -> None:
        """
        Program launcher.

        """
        while True:
            self.execute()

    def execute(self) -> None:
        """
        Executes the program.

        """
        print(Fore.LIGHTYELLOW_EX + f"SELECTED ROT TYPE: {self.rot.__name__} ")
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

    def change_rot(self) -> None:
        """
        The method for changing the cipher.

        """
        rot: str = get_valid_input("Set ROT: rot13/rot47: ", ["rot13", "rot47"]).lower()
        self.rot = get_rot(rot)

    def encode_decode(self, status: str) -> None:
        """
        A method used to encode and decode messages.

        """
        message: str = input("Write a message: ")
        modified_message: Message = Message(
            self.rot.__name__, self.rot.encode_decode(message), status
        )
        Buffer.add_message_to_buffer(modified_message)
