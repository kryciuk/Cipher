from functionality.rot import Rot13


class TestRot13:
    def test_should_return_encrypted_message_for_string_without_spaces_or_special_characters(
        self,
    ):
        self.base = "dog"

        assert Rot13.encode_decode(self.base) == "qbt"

    def test_should_return_encrypted_message_for_string_with_spaces(self):
        self.base = "He decided to fake his disappearance to avoid jail"

        assert (
            Rot13.encode_decode(self.base) == "Ur qrpvqrq "
            "gb snxr uvf qvfnccrnenapr gb nibvq wnvy"
        )

    def test_should_return_encrypted_message_for_string_with_punctuation(self):
        self.base = "Choosing to do nothing is still a choice, after all."

        assert (
            Rot13.encode_decode(self.base) == "Pubbfvat "
            "gb qb abguvat vf fgvyy n pubvpr, nsgre nyy."
        )

    def test_should_return_encrypted_message_for_string_with_numbers(self):
        self.base = "My favourite numbers are: 3, 726, 28."

        assert Rot13.encode_decode(self.base) == "Zl snibhevgr ahzoref ner: 3, 726, 28."


# https://www.dcode.fr/rot-13-cipher
