from datetime import datetime
from menu import Menu
from file_handler import FileHandler


class Message:
    def __init__(self, rot_type, text, status):
        self.rot_type = rot_type
        self.text = text
        self.status = status
        self.created_at = datetime.now()

    def __str__(self):
        return f"Rot type: {self.rot_type}\nText: {self.text}\nStatus: {self.status}\nCreated: {self.created_at}"

    def to_dct(self):
        mess_dict = {
            "type": self.rot_type,
            "text": self.text,
            "status": self.status,
            "creation": self.created_at.strftime("%d-%m-%y %H:%M"),
        }
        return mess_dict


class Buffer:
    buffer = []

    @staticmethod
    def buffer_menu():
        Menu.buffer_main_menu()
        choice = input()
        choice = choice_int_checker(choice)
        match choice:
            case 1:
                Buffer.show_buffer()
                Buffer.buffer_menu()
            case 2:
                Buffer.clear_buffer()
                Buffer.buffer_menu()
            case 3:
                file_name = input("Enter the name of the .json file: ") + ".json"
                FileHandler.save_from_buffer(file_name, Buffer.buffer)
                Buffer.clear_buffer()
                Buffer.buffer_menu()
                pass
            case 4:
                pass
            case _:
                print("Incorrect choice")

    @staticmethod
    def show_buffer():
        print(Buffer.buffer)

    @staticmethod
    def clear_buffer():
        return Buffer.buffer.clear()


def choice_int_checker(choice):
    try:
        choice = int(choice)
    except ValueError:
        pass
    return choice
