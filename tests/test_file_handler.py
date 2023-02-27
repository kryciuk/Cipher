from unittest.mock import patch
from file_handler.file_handler import FileHandler


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

    @patch("file_handler.file_handler.FileHandler.load_file")
    def test_should_open_file(self, mock_load_file):
        result = TestFileHandler.json_test_content
        mock_load_file.return_value = result

        assert FileHandler.load_file("test.json") == result

    @patch("file_handler.file_handler.FileHandler.save")
    def test_should_save_file(self, mock_save):
        result = TestFileHandler.json_test_content
        mock_save.return_value = result

        assert FileHandler.save("test.json") == result
