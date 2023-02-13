def choice_int_checker(choice):
    try:
        choice = int(choice)
    except ValueError:
        pass
    return choice
