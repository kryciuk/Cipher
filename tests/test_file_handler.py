import json
from file_handler.file_handler import FileHandler
from os.path import isfile
import os


class TestFileHandler:
    json_test_content = {
        "data": [
            {
                "rot_type": "Rot13",
                "text": "FUQUQUUQ",
                "status": "encoded",
                "creation": "13-02-23 22:29",
            }
        ]
    }

    def test_should_open_file(self):
        with open("test.json", "w+") as file:
            json.dump(TestFileHandler.json_test_content, file)
            file.seek(0)
        content = FileHandler.load("test.json")

        assert content == TestFileHandler.json_test_content
        os.remove("test.json")

    def test_should_save_file(self):
        FileHandler.save("test1.json", TestFileHandler.json_test_content)

        assert isfile("test1.json") and os.access("test1.json", os.R_OK)
        os.remove("test1.json")
