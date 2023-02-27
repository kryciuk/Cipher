from functionality.rot import Rot47


class TestRot47:
    def test_should_return_encrypted_message_for_string_without_spaces_or_special_characters(
        self,
    ):
        self.base = "dog"

        assert Rot47.encode_decode(self.base) == "5@8"

    def test_should_return_encrypted_message_for_string_with_spaces(self):
        self.base = "He decided to fake his disappearance to avoid jail"

        assert (
            Rot47.encode_decode(self.base) == "w6 564:565"
            " E@ 72<6 9:D 5:D2AA62C2?46 E@ 2G@:5 ;2:="
        )

    def test_should_return_encrypted_message_for_string_with_punctuation(self):
        self.base = "Choosing to do nothing is still a choice, after all."

        assert (
            Rot47.encode_decode(self.base) == "r9@@D:?8 E@ 5@ "
            "?@E9:?8 :D DE:== 2 49@:46[ 27E6C 2==]"
        )

    def test_should_return_encrypted_message_for_string_with_numbers(self):
        self.base = "My favourite numbers are: 3, 726, 28."

        assert Rot47.encode_decode(self.base) == "|J 72G@FC:E6 ?F>36CD 2C6i b[ fae[ ag]"


# https://www.dcode.fr/rot-13-cipher
