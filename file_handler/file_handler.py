import json
from typing import Dict, List


class FileHandler:
    """
    A class for reading and saving files.


    Methods
    ----------
    load
        Loads the contents of a file.
    save
        Saves the contents to a file.
    """

    @staticmethod
    def load(file_name: str) -> str:
        """
        Loads the contents of a file.

            Parameters:
                    file_name (str): The name of the file to be loaded.

            Returns:
                    data (str): Content read from file.
        """
        with open(file_name) as file:
            data: str = json.load(file)
        return data

    @staticmethod
    def save(file_name: str, buffer_content: Dict[str, List[Dict]]) -> None:
        """
        Saves the content of Buffer to a file.

            Parameters:
                    file_name (str): The name of the file to which the contents of the Buffer will be saved.
                    buffer_content (Dict): Buffer content.

        """
        with open(file_name, "w+") as file:
            json.dump(buffer_content, file)
