from menu.menu import Menu
from rot_operations.rot_operations import RotOperations


class Manager:
    def start(self):
        while True:
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
                return RotOperations.encoding()
            case 2:
                return RotOperations.decoding()
            case 3:
                # del Buffer
                exit()
            case _:
                print("Incorrect choice")
