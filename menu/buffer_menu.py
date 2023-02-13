from validators import choice_int_checker
from menu import Menu
from buffer import Buffer
from colorama import Fore


class BufferMenu:
    @staticmethod
    def buffer_main_menu():
        print(
            Fore.LIGHTCYAN_EX + "Buffer main menu:\n1 - Show buffer"
            "\n2 - Clear buffer\n3 - Return to "
            "main menu"
        )

    @staticmethod
    def buffer_menu():
        BufferMenu.buffer_main_menu()
        choice = input()
        choice = choice_int_checker(choice)
        match choice:
            case 1:
                Buffer.show_buffer()
                BufferMenu.buffer_menu()
            case 2:
                Buffer.clear_buffer()
                BufferMenu.buffer_menu()
            case 3:
                pass
            case _:
                print("Incorrect choice")
