from menu.menu import Menu
from rot_operations.rot_operations import RotOperations
from buffer.buffer import Buffer
from functionality import get_rot


class Manager:
    def __init__(self):
        self.rot = None

    def start(self):
        while True:
            self.show_menu()
            self.execute()

    def show_menu(self):
        print(f"SELECTED ROT TYPE {self.rot} ")
        Menu.main_menu()

    def execute(self):
        choice = int(input())
        match choice:
            case 1:
                return RotOperations.encoding()
            case 2:
                return RotOperations.decoding()
            case 3:
                self.__show_buffer
            case 4:
                Buffer.buffer.clear()
                exit()
            case 5:
                print("Set ROT, rot13/rot47")
                rot = ""
                while rot not in ["rot13", "rot47"]:
                    rot = input("Wybierz rot:")
                self.rot = get_rot(rot)

            case _:
                print("Incorrect choice")

    def __show_buffer(self):
        for idx, text in enumerate(Buffer.buffer, start=1):
            print(idx, text)
