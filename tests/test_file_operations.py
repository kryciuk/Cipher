import json
from menu import file_operations
from buffer import Message
import datetime
from unittest.mock import patch


class TestFileOperations:
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

    def test_should_convert_from_json_file_to_dict_with_Message_objects(self):
        with open("test.json", "w+") as file:
            json.dump(TestFileOperations.json_test_content, file)
            file.seek(0)
        result = file_operations.loading_from_file("test.json")

        assert result == {
            "data": [
                Message(
                    rot_type="Rot13",
                    text="FUQUQUUQ",
                    status="encoded",
                    creation=datetime.datetime(2023, 2, 13, 22, 29),
                )
            ]
        }

    @patch("builtins.input", return_value="file_name")
    def test_should_get_file_name_from_user_and_add_json(self, mock_input):
        result = file_operations.get_file_name()

        assert result == "file_name.json"
