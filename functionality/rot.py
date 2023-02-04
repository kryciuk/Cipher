from abc import ABC, abstractmethod
from typing import List
from string import ascii_uppercase


class Rot(ABC):
    """
    Representation of a class for encrypting and decrypting messages using a cipher.

    ...

    Methods
    -------
    encode(text)
        Encodes a message.
    decode(text)
        Decodes a message.
    """

    @staticmethod
    @abstractmethod
    def encode(text):
        """
        Returns an encoded message using a cipher.
        """
        pass

    @staticmethod
    @abstractmethod
    def decode(text):
        """
        Returns a decoded message using a cipher.
        """
        pass


class Rot13(Rot):
    """
    A class for encrypting and decrypting messages using Rot13 cipher.

    ...

    Methods
    -------
    encode(text)
        Encodes a message using Rot13.
    decode(text)
        Decodes a message using Rot13.
    """

    def __repr__(self):
        return "Rot13"

    @staticmethod
    def encode(text: str) -> str:
        """
        Returns an encoded message using Rot13 cipher.

            Parameters:
                    text (str): The message to be encoded

            Returns:
                    encoded_message (str): The encoded message
        """
        text = text.upper()
        encoded: List[str] = []
        for letter in text:
            if not letter.isalpha():
                encoded.append(letter)
                continue
            encoded_index: int = ascii_uppercase.index(letter) + 13
            if encoded_index >= 26:
                encoded_index -= 26
            encoded.append(ascii_uppercase[encoded_index])
        encoded_message: str = "".join(encoded)
        return encoded_message

    @staticmethod
    def decode(text: str) -> str:
        """
        Returns a decoded message using Rot13 cipher.

            Parameters:
                    text (str): The message to be decoded

            Returns:
                    decoded_message (str): The decoded message
        """
        text = text.upper()
        decoded: List[str] = []
        for letter in text:
            if not letter.isalpha():
                decoded.append(letter)
                continue
            decoded_index: int = ascii_uppercase.index(letter) - 13
            if decoded_index < 0:
                decoded_index += 26
            decoded.append(ascii_uppercase[decoded_index])
        decoded_message: str = "".join(decoded)
        return decoded_message


class Rot47(Rot):
    """
    A class for encrypting and decrypting messages using Rot47 cipher.

    ...

    Methods
    -------
    encode(text)
        Encodes a message using Rot47.
    decode(text)
        Decodes a message using Rot47.
    """

    key_rot47: List[str] = [chr(num) for num in range(33, 127)]

    def __repr__(self):
        return "Rot47"

    @classmethod
    def encode(cls, text: str) -> str:
        """
        Returns an encoded message using Rot47 cipher.

            Parameters:
                    text (str): The message to be encoded

            Returns:
                    encoded_message (str): The encoded message
        """
        encoded: List[str] = []
        for character in text:
            if character not in cls.key_rot47:
                encoded.append(character)
                continue
            encoded_index: int = cls.key_rot47.index(character) + 47
            if encoded_index >= 94:
                encoded_index -= 94
            encoded.append(cls.key_rot47[encoded_index])
        encoded_message: str = "".join(encoded)
        return encoded_message

    @classmethod
    def decode(cls, text: str) -> str:
        """
        Returns a decoded message using Rot47 cipher.

            Parameters:
                    text (str): The message to be decoded

            Returns:
                    decoded_message (str): The decoded message
        """
        decoded: List[str] = []
        for character in text:
            if character not in cls.key_rot47:
                decoded.append(character)
                continue
            encoded_index: int = cls.key_rot47.index(character) - 47
            if encoded_index < 0:
                encoded_index += 94
            decoded.append(cls.key_rot47[encoded_index])
        decoded_message: str = "".join(decoded)
        return decoded_message


def get_rot(rot_type):
    if rot_type == "rot13":
        return Rot13
    elif rot_type == "rot47":
        return Rot47
