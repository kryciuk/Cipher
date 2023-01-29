from functionality.rot import Rot47, Rot13


class FileOperations:
    @classmethod
    def encrypt_add_rot13(cls, file_name):
        with open(file_name, "a+") as file:
            file.seek(0)
            lines = file.read()
            lines_encoded = Rot13.encode(lines)
            file.write(lines_encoded)

    #        Buffer.buffer.append({"type": "rot13", "text": lines_encoded, "status": "encrypted"})

    @classmethod
    def encrypt_create_rot13(cls, file_name, new_file_name):
        with open(file_name, "r") as file:
            lines = file.read()
        with open(new_file_name, "w") as file:
            text = Rot13.encode(lines)
            file.write(text)

    #        Buffer.buffer.append({"type": "rot13", "text": text, "status": "encrypted"})

    @classmethod
    def encrypt_add_rot47(cls, file_name):
        with open(file_name, "a+") as file:
            file.seek(0)
            lines = file.read()
            lines_encoded = Rot47.encode(lines)
            file.write(lines_encoded)

    #        Buffer.buffer.append({"type": "rot47", "text": lines_encoded, "status": "encrypted"})

    @classmethod
    def encrypt_create_rot47(cls, file_name, new_file_name):
        with open(file_name, "r") as file:
            lines = file.read()
        with open(new_file_name, "w") as file:
            text = Rot47.encode(lines)
            file.write(text)

    #        Manager.buffer.append({"type": "rot47", "text": text, "status": "encrypted"})

    @classmethod
    def decrypt_add_rot13(cls, file_name):
        with open(file_name, "a+") as file:
            file.seek(0)
            lines = file.read()
            lines_decoded = Rot13.decode(lines)
            file.write(lines_decoded)

    #        Manager.buffer.append({"type": "rot13", "text": lines_decoded, "status": "decrypted"})

    @classmethod
    def decrypt_create_rot13(cls, file_name, new_file_name):
        with open(file_name, "r") as file:
            lines = file.read()
        with open(new_file_name, "w") as file:
            text = Rot13.decode(lines)
            file.write(text)

    #        Manager.buffer.append({"type": "rot13", "text": text, "status": "decrypted"})

    @classmethod
    def decrypt_add_rot47(cls, file_name):
        with open(file_name, "a+") as file:
            file.seek(0)
            lines = file.read()
            lines_decoded = Rot47.decode(lines)
            file.write(lines_decoded)

    #        Manager.buffer.append({"type": "rot47", "text": lines_decoded, "status": "decrypted"})

    @classmethod
    def decrypt_create_rot47(cls, file_name, new_file_name):
        with open(file_name, "r") as file:
            lines = file.read()
        with open(new_file_name, "w") as file:
            text = Rot47.decode(lines)
            file.write(text)


#        Manager.buffer.append({"type": "rot47", "text": text, "status": "decrypted"})
