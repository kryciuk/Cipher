from functionality.rot import Rot13


class TestRot13:
    def test_should_return_encrypted_message_for_string_without_spaces_or_special_characters(
        self,
    ):
        self.base = "dog"

        assert Rot13.encode(self.base) == "qbt".upper()

    def test_should_return_encrypted_message_for_string_with_spaces(self):
        self.base = "He decided to fake his disappearance to avoid jail"

        assert (
            Rot13.encode(self.base) == "Ur qrpvqrq gb snxr uvf qvfnccrnenapr gb nibvq wnvy".upper()
        )

    def test_should_return_encrypted_message_for_string_with_punctuation(self):
        self.base = "Choosing to do nothing is still a choice, after all."

        assert (
            Rot13.encode(self.base) == "Pubbfvat gb qb abguvat vf fgvyy n pubvpr, nsgre nyy.".upper()
        )

    def test_should_return_encrypted_message_for_string_with_numbers(self):
        self.base = "My favourite numbers are: 3, 726, 28."

        assert (
            Rot13.encode(self.base) == "Zl snibhevgr ahzoref ner: 3, 726, 28.".upper()
        )


# https://www.dcode.fr/rot-13-cipher
