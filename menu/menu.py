from colorama import Fore


class Menu:
    @staticmethod
    def show_menu():
        print(
            Fore.GREEN + "What do you want to do?\n1 - encode "
            "file\n2 - decode file\n3 - end program"
        )

    @staticmethod
    def get_choice():
        return int(input())

    @staticmethod
    def rot_choice():
        print(
            Fore.MAGENTA + "Enter the number corresponding to the "
            "cipher you want to use:\n1 - Rot13\n2 - Rot47"
        )

    @staticmethod
    def file_choice():
        print(
            Fore.CYAN + "Add the encoded message to an existing file "
            "or create a new one?\n1 - Add\n2 - Create new"
        )
