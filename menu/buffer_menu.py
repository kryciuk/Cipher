from validators import get_valid_input
from menu import Menu
from buffer import Buffer
from colorama import Fore


class BufferMenu:
    """
    A class representing the Buffer menu.
    ...

    Attributes
    ----------
    BUFFER_MENU_PROMPT : str
        Shows the possible options to choose from the menu.

    Methods
    ----------
    buffer_menu
        A method that displays the menu and gets the response from the user.

    """

    BUFFER_MENU_PROMPT: str = (
        Fore.LIGHTCYAN_EX + "Buffer main menu:\n1 - Show buffer \n"
        "2 - Clear buffer\n3 - Return to main menu\n"
    )

    @staticmethod
    def buffer_menu() -> None:
        """
        A method that displays the menu and gets the response from the user.

        """
        choice: str = get_valid_input(BufferMenu.BUFFER_MENU_PROMPT, ["1", "2", "3"])
        match choice:
            case "1":
                Buffer.show_buffer()
            case "2":
                Buffer.clear_buffer()
            case "3":
                return
        BufferMenu.buffer_menu()
