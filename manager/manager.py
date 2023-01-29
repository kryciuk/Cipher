from menu.menu import Menu
from rot_operations.rot_operations import RotOperations
from buffer.buffer import Buffer


class Manager:
    def start(self):
        while True:
            self.show_menu()
            self.execute()

    @staticmethod
    def show_menu():
        Menu.main_menu()

    @staticmethod
    def execute():
        choice = int(input())
        match choice:
            case 1:
                return RotOperations.encoding_decoding()
            case 2:
                return RotOperations.encoding_decoding()
            case 3:
                print(Buffer.buffer)
            case 4:
                Buffer.buffer.clear()
                exit()
            case _:
                print("Incorrect choice")
