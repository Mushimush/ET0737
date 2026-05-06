from FileHandler import FileHandler
import csv


class CsvFile(FileHandler):
    def read(self):
        rows = []
        with open(self.filepath, "r", encoding="utf-8", newline="") as file:
            reader = csv.reader(file)
            print("reader:", reader)  # Debug: check the type of reader
            for row in reader:
                print("row:", row)  # Debug: check the content of each row
                rows.append(row)
        return rows
