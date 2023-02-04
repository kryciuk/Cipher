from datetime import datetime


class Message:
    def __init__(self, rot_type, text, status):
        self.rot_type = rot_type
        self.text = text
        self.status = status
        self.created_at = datetime.now()

    def __repr__(self):
        pass

    def to_dct(self):
        mess_dict = {
            "type": self.rot_type,
            "text": self.text,
            "status": self.status,
            "creation": self.created_at,
        }
        return mess_dict


class Buffer:
    buffer = []
