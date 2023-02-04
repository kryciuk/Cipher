import json


class FileHandler:
    @staticmethod
    def load_message(file_name):
        with open(file_name, "r") as file:
            file.seek(0)
            lines = json.load(file)
        return lines

    @staticmethod
    def save_to_existing():
        pass

    @staticmethod
    def save_to_new(file_name, message):
        with open(file_name, "w+") as file:
            json.dump(message, file)
