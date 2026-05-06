from FileHandler import FileHandler
import json


# ============================================================
# KEY CONCEPT: INHERITANCE
# ------------------------------------------------------------
# The "(FileHandler)" below means JsonFile INHERITS from
# FileHandler. JsonFile automatically gets:
#   - __init__(self, filepath)   -> from the parent
#   - self.filepath              -> from the parent
#   - filesize()                 -> from the parent
# We do NOT rewrite any of those. We only add what is unique
# to JSON files: how to read them.
# ============================================================
class JsonFile(FileHandler):

    # ============================================================
    # KEY CONCEPT: POLYMORPHISM (via METHOD OVERRIDING)
    # ------------------------------------------------------------
    # The parent FileHandler defines read() but it only raises
    # NotImplementedError. Here we OVERRIDE it with a JSON-specific
    # version. CsvFile and LogFile will override the same method
    # with their own logic.
    #
    # This means a caller can write `handler.read()` without
    # knowing whether `handler` is a JsonFile, CsvFile, or LogFile
    # -- Python picks the right version automatically. That is
    # polymorphism: ONE method name, MANY behaviours.
    # ============================================================
    def read(self):
        # TODO:
        # Open self.filepath and use json.load(file) to parse it.
        # Return the resulting Python object (usually a dict).
        # Hint: use a `with open(...) as file:` block so the file
        # closes automatically.
        pass
