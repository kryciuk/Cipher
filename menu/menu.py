from colorama import Fore


class Menu:
    """
    A class representing the Main Menu.
    ...

    Attributes
    ----------
    main_menu : str
        Shows the possible options to choose from the menu.

    """

    main_menu: str = (
        Fore.LIGHTGREEN_EX + "What do you want to do?\n1 - Change rot\n2 - Encode\n"
        "3 - Decode\n4 - Buffer menu\n5 - File Operations menu\n6 - End program\n"
    )
