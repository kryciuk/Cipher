from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List

from colorama import Fore


@dataclass
class Message:
    """
    A class representing the encoded/decoded message.

    ...
    Attributes
    ----------
    rot_type : str
        The name of used cipher.
    text : str
        Textual content of the message.
    status : str
        Status of the message - encoded/decoded.
    creation : datetime
        Time of creation.


    Methods
    ----------
    to_dct
        Converts the Message object into a dictionary.
    from_dct
        Creates a Message object from the dictionary.
    """

    rot_type: str
    text: str
    status: str
    creation: datetime = datetime.now()

    def __str__(self) -> str:
        time_as_string: str = self.creation.strftime("%d-%m-%y %H:%M")
        return (
            f"Rot type: {self.rot_type : <10}Status: {self.status : <12}"
            f"Created: {time_as_string: <19}Text: {self.text} "
        )  # self.creation:%d-%m-%y %H:%M

    def to_dct(self) -> Dict:
        """
        Converts the Message object into a dictionary.

            Returns:
                    mess_dict (Dict): The Message presented in the form of a dictionary.
        """
        mess_dict: Dict = {
            "rot_type": self.rot_type,
            "text": self.text,
            "status": self.status,
            "creation": self.creation.strftime("%d-%m-%y %H:%M"),
        }
        return mess_dict

    @classmethod
    def from_dct(cls, dct: Dict) -> "Message":
        """
        Creates a Message object from the dictionary.

            Parameters:
                    dct (Dict): A dictionary to be processed into Message.

            Returns:
                    unpacked (Message): The Message object.
        """
        unpacked = cls(**dct)
        if not isinstance(unpacked.creation, datetime):
            unpacked.creation = datetime.strptime(unpacked.creation, "%d-%m-%y %H:%M")
        return unpacked


class Buffer:
    """
    A class representing a place to store Message objects.

    ...
    Attributes
    ----------
    buffer:
        Dictionary storing Message objects.

    ----------

    Methods
    -------
    show_buffer:
        Shows the contents of Buffer.
    clear_buffer:
        Cleans Buffer from the contents.
    add_message_to_buffer:
        Adds Message object to Buffer.
    transform_to_dict:
        Converts all Message objects in the Buffer into dictionaries.
    """

    buffer: Dict[str, List[Message]] = {"data": []}

    @staticmethod
    def show_buffer() -> None:
        """
        Shows the contents of Buffer.

        """
        if not Buffer.buffer["data"]:
            print(Fore.LIGHTMAGENTA_EX + "Buffer is empty.")
        elif Buffer.buffer["data"]:
            print(Fore.LIGHTMAGENTA_EX + "Buffer:")
            for obj in enumerate(Buffer.buffer["data"]):
                print(Fore.LIGHTMAGENTA_EX + f"{obj[0] + 1}. {obj[1]}")

    @staticmethod
    def clear_buffer() -> None:
        """
        Cleans the contents of Buffer.

        """
        Buffer.buffer["data"].clear()

    @staticmethod
    def add_message_to_buffer(message: Message) -> None:
        """
        Adds new Message to Buffer.

            Parameters:
                    message (Message): Message object to be added to the Buffer.

        """
        Buffer.buffer["data"].append(message)

    @staticmethod
    def transform_to_dict():
        """
        Converts the entire contents of the Buffer into a dictionary containing dictionaries created from Message objects.

            Returns:
                    dct (Dict): A dictionary containing dictionaries created from Message objects.

        """
        return {"data": [entry.to_dct() for entry in Buffer.buffer.get("data")]}


if __name__ == "__main__":
    print(Buffer.buffer.get("data"))
    print(Buffer.transform_to_dict())
