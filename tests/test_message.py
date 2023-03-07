import datetime

from buffer import Message


class TestMessage:
    def test_should_display_message_as_dict(self):
        base = Message(
            "rot13", "Hello", "decoded", datetime.datetime(2022, 12, 28, 23, 55)
        )

        assert base.to_dct() == {
            "rot_type": "rot13",
            "text": "Hello",
            "status": "decoded",
            "creation": "28-12-22 23:55",
        }

    def test_should_transform_dict_to_Message_object(self):
        base = {
            "rot_type": "rot47",
            "text": "<C6H6E<2",
            "status": "encoded",
            "creation": "30-01-23 00:01",
        }

        assert Message.from_dct(base) == Message(
            "rot47", "<C6H6E<2", "encoded", datetime.datetime(2023, 1, 30, 00, 1)
        )
