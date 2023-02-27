from buffer import Buffer, Message
import datetime
from freezegun import freeze_time
from colorama import Fore


class TestMessage:
    def test_should_clear_buffer(self):
        Buffer.buffer = {
            "data": [
                Message(
                    rot_type="rot13",
                    text="Hello",
                    status="encoded",
                    creation=datetime.datetime(2023, 2, 21, 17, 50, 26, 291600),
                )
            ]
        }
        Buffer.clear_buffer()

        assert Buffer.buffer == {"data": []}

    @freeze_time("2012-01-14 10:10:08")
    def test_should_add_message_to_buffer_if_buffer_was_empty(self):
        Buffer.buffer = {"data": []}
        test_message1 = Message(
            "rot13", "uryyb gurer", "encoded", datetime.datetime.now()
        )
        Buffer.add_message_to_buffer(test_message1)

        assert Buffer.buffer == {
            "data": [
                Message(
                    rot_type="rot13",
                    text="uryyb gurer",
                    status="encoded",
                    creation=datetime.datetime(2012, 1, 14, 10, 10, 8),
                )
            ]
        }

    @freeze_time("2023-02-01 08:08:08")
    def test_should_add_message_to_buffer_if_buffer_was_not_empty(self):
        Buffer.buffer = {
            "data": [
                Message(
                    rot_type="rot13",
                    text="Hello",
                    status="encoded",
                    creation=datetime.datetime(2023, 2, 21, 17, 50, 26, 291600),
                )
            ]
        }
        test_message1 = Message("rot47", "qbttbf", "encoded", datetime.datetime.now())
        Buffer.add_message_to_buffer(test_message1)

        assert Buffer.buffer == {
            "data": [
                Message(
                    rot_type="rot13",
                    text="Hello",
                    status="encoded",
                    creation=datetime.datetime(2023, 2, 21, 17, 50, 26, 291600),
                ),
                Message(
                    rot_type="rot47",
                    text="qbttbf",
                    status="encoded",
                    creation=datetime.datetime(2023, 2, 1, 8, 8, 8),
                ),
            ]
        }

    def test_should_transform_buffer_entries_to_dict(self):
        Buffer.buffer = {
            "data": [
                Message(
                    rot_type="rot13",
                    text="Hello",
                    status="encoded",
                    creation=datetime.datetime(2023, 2, 21, 17, 50, 26, 291600),
                ),
                Message(
                    rot_type="rot47",
                    text="qbttbf",
                    status="encoded",
                    creation=datetime.datetime(2023, 2, 1, 8, 8, 8),
                ),
            ]
        }
        test_result = Buffer.transform_to_dict()

        assert test_result == {
            "data": [
                {
                    "rot_type": "rot13",
                    "text": "Hello",
                    "status": "encoded",
                    "creation": "21-02-23 17:50",
                },
                {
                    "rot_type": "rot47",
                    "text": "qbttbf",
                    "status": "encoded",
                    "creation": "01-02-23 08:08",
                },
            ]
        }

    def test_should_show_buffer_if_buffer_was_empty(self, capsys):
        Buffer.buffer = {"data": []}
        Buffer.show_buffer()
        captured = capsys.readouterr()

        assert captured.out == Fore.LIGHTMAGENTA_EX + "Buffer is empty.\n"

    def test_should_show_buffer_if_buffer_was_not_empty(self, capsys):
        Buffer.buffer = {
            "data": [
                Message(
                    rot_type="rot13",
                    text="Hello",
                    status="encoded",
                    creation=datetime.datetime(2023, 2, 21, 17, 50, 26, 291600),
                )
            ]
        }
        Buffer.show_buffer()
        captured = capsys.readouterr()

        assert (
            captured.out == Fore.LIGHTMAGENTA_EX + "Buffer:"
            "\n" + Fore.LIGHTMAGENTA_EX + "1. "
            "Rot type: rot13     Status: encoded     Created: 21-02-23 17:50     Text: Hello \n"
        )
