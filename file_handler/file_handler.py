from functionality.rot import Rot47, Rot13
from buffer.buffer import Buffer


class FileOperations:
    @staticmethod
    def encrypt(choice, file_name, rot, new_file_name=None):
        with open(file_name, "a+") as file:
            file.seek(0)
            lines = file.read()
            if rot == 1:
                lines_encoded = Rot13.encode(lines)
                _type = "Rot13"
            elif rot == 2:
                lines_encoded = Rot47.encode(lines)
                _type = "Rot47"
            if choice == 1:
                file.write(lines_encoded)
            elif choice == 2:
                with open(new_file_name, "w+") as new_file:
                    new_file.write(lines_encoded)
            Buffer.buffer.append(
                {"type": _type, "text": lines_encoded, "status": "encrypted"}
            )

    @staticmethod
    def decrypt(choice, file_name, rot, new_file_name=None):
        with open(file_name, "a+") as file:
            file.seek(0)
            lines = file.read()
            if rot == 1:
                lines_decoded = Rot13.decode(lines)
                _type = "Rot13"
            elif rot == 2:
                lines_decoded = Rot47.decode(lines)
                _type = "Rot47"
            if choice == 1:
                file.write(lines_decoded)
            elif choice == 2:
                with open(new_file_name, "w+") as new_file:
                    new_file.write(lines_decoded)
            Buffer.buffer.append(
                {"type": _type, "text": lines_decoded, "status": "decrypted"}
            )
