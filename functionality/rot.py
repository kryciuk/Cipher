from abc import ABC, abstractmethod
import re


class Rot(ABC):

    @abstractmethod
    def encode(self, text):
        pass

    @abstractmethod
    def decode(self, text):
        pass


class Rot13(Rot):
    key_rot13 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    @classmethod
    def encode(cls, text):
        text = text.upper()
        encoded = []
        for i in text:
            if re.match(r"[\s\W\d]", i):
                encoded.append(i)
                continue
            encoded_index = cls.key_rot13.index(i) + 13
            if encoded_index >= 26:
                encoded_index -= 26
            encoded.append(cls.key_rot13[encoded_index])
        return "".join(encoded)

    @classmethod
    def decode(cls, text):
        text = text.upper()
        decoded = []
        for i in text:
            if re.match(r"[\s\W\d]", i):
                decoded.append(i)
                continue
            decoded_index = cls.key_rot13.index(i) - 13
            if decoded_index < 0:
                decoded_index += 26
            decoded.append(cls.key_rot13[decoded_index])
        return "".join(decoded)


class Rot47(Rot):
    key_rot47 = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"

    @classmethod
    def encode(cls, text):
        encoded = []
        for i in text:
            if re.match(r" ", i):
                encoded.append(i)
                continue
            encoded_index = cls.key_rot47.index(i) + 47
            if encoded_index >= 94:
                encoded_index -= 94
            encoded.append(cls.key_rot47[encoded_index])
        return "".join(encoded)

    @classmethod
    def decode(cls, text):
        decoded = []
        for i in text:
            if re.match(r" ", i):
                decoded.append(i)
                continue
            encoded_index = cls.key_rot47.index(i) - 47
            if encoded_index < 0:
                encoded_index += 94
            decoded.append(cls.key_rot47[encoded_index])
        return "".join(decoded)


def main():
    print(Rot13.encode("Joe waited for the train."))
    print(Rot13.decode("Wbr jnvgrq sbe gur genva."))
    print(Rot47.encode("Joe waited for the train."))
    print(Rot47.decode("y@6 H2:E65 7@C E96 EC2:?]"))


if __name__ == "__main__":
    main()

#https://www.dcode.fr/rot-13-cipher
#https://www.dcode.fr/rot-47-cipher
