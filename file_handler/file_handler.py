import json


class FileHandler:
    @staticmethod
    def load_file(file_name):
        with open(file_name) as file:
            data = json.load(file)
        return data

    @staticmethod
    def save_to_new(file_name, buffer_content):
        with open(file_name, "w+") as file:
            json.dump(buffer_content, file)

    # @staticmethod
    # def append_to_existing(file_name, buffer_content):
    #     with open(file_name, "a+") as file:
    #         file.seek(0)
    #         json.dump(buffer_content, file)
