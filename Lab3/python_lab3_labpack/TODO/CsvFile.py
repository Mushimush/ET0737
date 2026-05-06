from FileHandler import FileHandler
import csv


# ============================================================
# KEY CONCEPT: INHERITANCE
# ------------------------------------------------------------
# CsvFile is a CHILD CLASS of FileHandler.
# It reuses __init__, self.filepath, and filesize() from the
# parent for free -- we never rewrite them here.
# ============================================================
class CsvFile(FileHandler):

    # ============================================================
    # KEY CONCEPT: POLYMORPHISM (via METHOD OVERRIDING)
    # ------------------------------------------------------------
    # Same method name as JsonFile.read() and LogFile.read(),
    # but DIFFERENT behaviour: this one parses CSV rows.
    # The caller doesn't care which class it has -- calling
    # .read() always does "the right thing" for that file type.
    # ============================================================
    def read(self):
        # TODO:
        # Open self.filepath, create a csv.reader(file),
        # loop through it, and collect each row into a list.
        # Return the list of rows.
        pass
