from functionality.rot import get_rot, Rot47, Rot13


class TestGetRot:
    def test_should_return_Rot47(self):
        self.base = "rot47"

        assert get_rot(self.base) is Rot47

    def test_should_return_Rot13(self):
        self.base = "rot13"

        assert get_rot(self.base) is Rot13

    def test_should_return_None(self):
        self.base = "dog"

        assert get_rot(self.base) is None
