from FileHandler import FileHandler
import re


class LogFile(FileHandler):
    def read(self):
        error_lines = []
        pattern = r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} \[Error\] .+$"

        with open(self.filepath, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if re.match(pattern, line):
                    error_lines.append(line)

        return error_lines
