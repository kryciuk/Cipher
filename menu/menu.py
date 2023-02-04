from colorama import Fore


class Menu:
    @staticmethod
    def main_menu():
        print(
            Fore.GREEN + "What do you want to do?\n1 - change rot\n"
            "2 - encode\n3 - decode\n4 - show buffer "
            "menu\n5 - end program "
        )

    @staticmethod
    def get_choice():
        return int(input())

    @staticmethod
    def write_load_menu():
        print(
            Fore.MAGENTA + "Do you want to write a message "
            "or load from a file?\n1 - Write\n2 - Load"
        )

    @staticmethod
    def save_or_buffer_menu():
        print(Fore.RED + "Save the message or add it to a buffer?\n1 - Save\n2 - Add")

    @staticmethod
    def new_or_existing_menu():
        print(
            Fore.BLUE + "Save the message to a new file, or add "
            "it to the file from which it was read?\n1 - New\n2 "
            "- Existing "
        )
