from datetime import datetime
from dataclasses import dataclass
import json


@dataclass
class Message:
    rot_type: str
    text: str
    status: str
    created_at: datetime = datetime.now()

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

    # @classmethod
    # def from_dct(cls, dct):
    #     return cls(**dct)


class Buffer:
    buffer = {"data": []}

    @staticmethod
    def show_buffer():
        print(Buffer.buffer)

    @staticmethod
    def clear_buffer():
        return Buffer.buffer["data"].clear()

    @staticmethod
    def add_message_to_buffer(message):
        Buffer.buffer["data"].append(message)
