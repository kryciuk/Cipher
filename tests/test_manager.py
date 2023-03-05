import pytest
from manager import Manager
from unittest.mock import patch
from functionality.rot import Rot47
from buffer import Buffer
from freezegun import freeze_time


class TestManager:
    @patch("builtins.input", return_value="rot47")
    def test_change_rot_valid_input(self, mock_input):
        manager = Manager()
        manager.change_rot()
        assert manager.rot == Rot47

    @freeze_time("2012-01-14 10:10:08")
    def test_encode_decode_should_create_Message_and_add_to_buffer(self):
        input_values = ["2", "message"]
        with patch("builtins.input", side_effect=input_values):
            manager = Manager()
            manager.execute()
            result = Buffer.buffer.get("data")
        assert result is not False

    @patch("builtins.input", return_value="6")
    def test_execute_should_close_program(self, mock_input):
        manager1 = Manager()
        with pytest.raises(SystemExit):
            manager1.execute()
