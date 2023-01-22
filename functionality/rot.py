from abc import ABC, abstractmethod
import re
from typing import List


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

    @abstractmethod
    def encode(self, text):
        """
        Returns an encoded message using a cipher.
        """
        pass

    @abstractmethod
    def decode(self, text):
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
    key_rot13: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    @classmethod
    def encode(cls, text: str) -> str:
        """
        Returns an encoded message using Rot13 cipher.

            Parameters:
                    text (str): The message to be encoded

            Returns:
                    encoded_message (str): The encoded message
        """
        text = text.upper()
        encoded: List[str] = []
        for i in text:
            if re.match(r"[\s\W\d]", i):
                encoded.append(i)
                continue
            encoded_index: int = cls.key_rot13.index(i) + 13
            if encoded_index >= 26:
                encoded_index -= 26
            encoded.append(cls.key_rot13[encoded_index])
        encoded_message: str = "".join(encoded)
        return encoded_message

    @classmethod
    def decode(cls, text: str) -> str:
        """
        Returns a decoded message using Rot13 cipher.

            Parameters:
                    text (str): The message to be decoded

            Returns:
                    decoded_message (str): The decoded message
        """
        text = text.upper()
        decoded: List[str] = []
        for i in text:
            if re.match(r"[\s\W\d]", i):
                decoded.append(i)
                continue
            decoded_index: int = cls.key_rot13.index(i) - 13
            if decoded_index < 0:
                decoded_index += 26
            decoded.append(cls.key_rot13[decoded_index])
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
    key_rot47: str = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"

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
        for i in text:
            if re.match(r" ", i):
                encoded.append(i)
                continue
            encoded_index: int = cls.key_rot47.index(i) + 47
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
        for i in text:
            if re.match(r" ", i):
                decoded.append(i)
                continue
            encoded_index: int = cls.key_rot47.index(i) - 47
            if encoded_index < 0:
                encoded_index += 94
            decoded.append(cls.key_rot47[encoded_index])
        decoded_message: str = "".join(decoded)
        return decoded_message


def main():
    print(Rot13.encode("Joe waited for the train."))
    print(Rot13.decode("Wbr jnvgrq sbe gur genva."))
    print(Rot47.encode("Joe waited for the train."))
    print(Rot47.decode("y@6 H2:E65 7@C E96 EC2:?]"))
    print(Rot47.decode.__doc__)
    print(Rot47.__doc__)


if __name__ == "__main__":
    main()

# https://www.dcode.fr/rot-13-cipher
# https://www.dcode.fr/rot-47-cipher
