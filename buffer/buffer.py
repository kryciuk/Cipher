from datetime import datetime
from dataclasses import dataclass
from colorama import Fore


@dataclass
class Message:
    rot_type: str
    text: str
    status: str
    creation: datetime = datetime.now()

    def __str__(self):
        time_as_string = self.creation.strftime("%d-%m-%y %H:%M")
        return f"Rot type: {self.rot_type}      Status: {self.status}       Created: {time_as_string}       Text: {self.text}"

    def to_dct(self):
        mess_dict = {
            "rot_type": self.rot_type,
            "text": self.text,
            "status": self.status,
            "creation": self.creation.strftime("%d-%m-%y %H:%M"),
        }
        return mess_dict

    @classmethod
    def from_dct(cls, dct):
        unpacked = cls(**dct)
        if not isinstance(unpacked.creation, datetime):
            unpacked.creation = datetime.strptime(unpacked.creation, "%d-%m-%y %H:%M")
        return unpacked


class Buffer:
    buffer = {"data": []}

    @staticmethod
    def show_buffer():
        if not Buffer.buffer["data"]:
            print(Fore.LIGHTMAGENTA_EX + "Buffer is empty.")
        elif Buffer.buffer["data"]:
            print(Fore.LIGHTMAGENTA_EX + "Buffer:")
            for obj in enumerate(Buffer.buffer["data"]):
                print(Fore.LIGHTMAGENTA_EX + f"{obj[0] + 1}. {obj[1]}")

    @staticmethod
    def clear_buffer():
        return Buffer.buffer["data"].clear()

    @staticmethod
    def add_message_to_buffer(message):
        Buffer.buffer["data"].append(message)

    @staticmethod
    def transform_to_dict():
        return {"data": [entry.to_dct() for entry in Buffer.buffer.get("data")]}
