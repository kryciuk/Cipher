from functionality.rot import Rot47, Rot13
from buffer.buffer import Buffer
import json


class FileOperations:
    @staticmethod
    def encrypt(choice, file_name, rot, new_file_name=None):
        with open(file_name, "r+") as file:
            lines = json.load(file)
            if rot == 1:
                lines_encoded = Rot13.encode(lines)
                rot_type = "Rot13"
            elif rot == 2:
                lines_encoded = Rot47.encode(lines)
                rot_type = "Rot47"
            if choice == 1:
                file.seek(0)
                json.dump(lines + " " + lines_encoded, file)
            elif choice == 2:
                with open(new_file_name, "w+") as new_file:
                    json.dump(lines_encoded, new_file)
            Buffer.buffer.append(
                {"type": rot_type, "text": lines_encoded, "status": "encrypted"}
            )

    @staticmethod
    def decrypt(choice, file_name, rot, new_file_name=None):
        with open(file_name, "a+") as file:
            file.seek(0)
            lines = json.load(file)
            if rot == 1:
                lines_decoded = Rot13.decode(lines)
                rot_type = "Rot13"
            elif rot == 2:
                lines_decoded = Rot47.encode(lines)
                rot_type = "Rot47"
            if choice == 1:
                file.seek(0)
                json.dump(lines + " " + lines_decoded, file)
            elif choice == 2:
                with open(new_file_name, "w+") as new_file:
                    json.dump(lines_decoded, new_file)
            Buffer.buffer.append(
                {"type": rot_type, "text": lines_decoded, "status": "decrypted"}
            )
