from abc import ABC, abstractmethod
from string import ascii_lowercase, ascii_uppercase
from typing import List, Type


class Rot(ABC):
    """
    Representation of a class for encrypting and decrypting messages using a cipher.

    ...

    Methods
    -------
    encode_decode(text)
        Method for both message encoding and decoding
    """

    @staticmethod
    @abstractmethod
    def encode_decode(text):
        """
        Returns an encoded or decoded message using a cipher.
        """
        pass


class Rot13(Rot):
    """
    A class for encrypting and decrypting messages using Rot13 cipher.

    ...

    Methods
    -------
    encode_decode(text)
        Method for both message encoding and decoding using Rot13.
    """

    def __repr__(self):
        return "Rot13"

    @staticmethod
    def encode_decode(text: str) -> str:
        """
        Returns an encoded or decoded message using Rot13 cipher.

            Parameters:
                    text (str): The message to be encoded/decoded

            Returns:
                    modified_message (str): The encoded/decoded message
        """
        modified: List[str] = []
        for letter in text:
            if not letter.isalpha():
                modified.append(letter)
                continue
            if letter.isupper():
                encoded_index_rot13: int = ascii_uppercase.index(letter) + 13
                if encoded_index_rot13 >= 26:
                    encoded_index_rot13 -= 26
                modified.append(ascii_uppercase[encoded_index_rot13])
            elif letter.islower():
                encoded_index: int = ascii_lowercase.index(letter) + 13
                if encoded_index >= 26:
                    encoded_index -= 26
                modified.append(ascii_lowercase[encoded_index])
        modified_message: str = "".join(modified)
        return modified_message


class Rot47(Rot):
    """
    A class for encrypting and decrypting messages using Rot47 cipher.

    ...

    Methods
    -------
    encode_decode(text)
        Method for both message encoding and decoding using Rot47.
    """

    key_rot47: List[str] = [chr(num) for num in range(33, 127)]

    def __repr__(self):
        return "Rot47"

    @classmethod
    def encode_decode(cls, text: str) -> str:
        """
        Returns an encoded message using Rot47 cipher.

            Parameters:
                    text (str): The message to be encoded/decoded

            Returns:
                    modified_message (str): The encoded/decoded message
        """
        modified: List[str] = []
        for character in text:
            if character not in cls.key_rot47:
                modified.append(character)
                continue
            encoded_index_rot47: int = cls.key_rot47.index(character) + 47
            if encoded_index_rot47 >= 94:
                encoded_index_rot47 -= 94
            modified.append(cls.key_rot47[encoded_index_rot47])
        modified_message: str = "".join(modified)
        return modified_message


def get_rot(rot_type: str) -> Type[Rot13 | Rot47] | None:
    """
    Returns the cipher type.

            cipher_type (Rot13 | Rot47 | None): Cipher type.
    """
    if rot_type == "rot13":
        return Rot13
    elif rot_type == "rot47":
        return Rot47
    return None
