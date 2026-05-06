
from FileHandler import FileHandler
import json


class JsonFile(FileHandler):
    def read(self):
        with open(self.filepath, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data
