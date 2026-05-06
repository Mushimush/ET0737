from FileHandler import FileHandler
import re


# ============================================================
# KEY CONCEPT: INHERITANCE
# ------------------------------------------------------------
# LogFile is another CHILD of FileHandler. Like JsonFile and
# CsvFile, it inherits __init__, self.filepath, and filesize().
# All three child classes share the same "shape" because they
# all extend the same parent.
# ============================================================
class LogFile(FileHandler):

    # ============================================================
    # KEY CONCEPT: POLYMORPHISM (via METHOD OVERRIDING)
    # ------------------------------------------------------------
    # Same method name (read), totally different job: filter the
    # log file down to lines that match the [Error] pattern using
    # regex. This is the third "form" of read() -- one method
    # name, many behaviours.
    #
    # BONUS CONCEPT: REGEX
    # ------------------------------------------------------------
    # Regex (regular expressions) lets us describe a text pattern
    # and ask "does this line match?" The pattern below matches:
    #   ^                  -> start of line
    #   \d{4}-\d{2}-\d{2}  -> YYYY-MM-DD date
    #   \d{2}:\d{2}:\d{2}  -> HH:MM:SS time
    #   \[Error\]          -> the literal text [Error]
    #   .+$                -> any message, up to end of line
    # re.match(pattern, line) returns a Match object (truthy) if
    # it matches, or None (falsy) if it doesn't.
    # ============================================================
    def read(self):
        error_lines = []
        pattern = r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} \[Error\] .+$"

        with open(self.filepath, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                # TODO:
                # If re.match(pattern, line) is truthy,
                # append line to error_lines.
                pass

        return error_lines
