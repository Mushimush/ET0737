import sys
import os


# ============================================================
# KEY CONCEPT: PARENT CLASS (the BASE for inheritance)
# ------------------------------------------------------------
# FileHandler is the PARENT class. JsonFile, CsvFile, and
# LogFile all inherit from it. Anything defined here is
# automatically available on every child class.
#
# Two things live here:
#   1. SHARED behaviour    -> __init__ and filesize()
#      (every child gets these for free, no rewriting)
#   2. A PROMISE / contract -> read()
#      (children MUST override this with their own version)
#
# This is the classic OOP setup for polymorphism:
#   - parent declares a method every child must provide
#   - each child supplies a different implementation
#   - calling .read() works on any child without caring which
# ============================================================
class FileHandler:
    def __init__(self, filepath):
        # Inherited by every child. They never rewrite this.
        self.filepath = filepath

    def filesize(self):
        """Return file size in bytes."""
        # Inherited by every child. They never rewrite this either.
        return os.path.getsize(self.filepath)

    def read(self):
        """Child classes must implement this method."""
        # Raising NotImplementedError forces every child class
        # to OVERRIDE this method. If a child forgets to define
        # read(), calling it will crash loudly instead of
        # silently doing nothing. This is how the parent enforces
        # the "contract" that every child must keep.
        raise NotImplementedError("Subclasses must implement read()")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 FileHandler.py <file_path>")
        return

    filepath = sys.argv[1]

    if not os.path.exists(filepath):
        print("Error: File does not exist")
        return

    ext = os.path.splitext(filepath)[1].lower()

    from JsonFile import JsonFile
    from CsvFile import CsvFile
    from LogFile import LogFile

    # ============================================================
    # KEY CONCEPT: POLYMORPHISM IN ACTION
    # ------------------------------------------------------------
    # Below, we pick which CHILD CLASS to instantiate based on
    # the file extension. Once we have `handler`, the rest of
    # main() just calls handler.filesize() and handler.read()
    # WITHOUT caring which type it actually is.
    #
    # That is the payoff of polymorphism: the same two lines
    # at the bottom of main() work for JSON, CSV, and Log files.
    # If we add an XmlFile class tomorrow, only this if/elif
    # block changes -- the print lines stay identical.
    # ============================================================
    # TODO:
    # Choose the correct child class based on file extension
    # .json -> JsonFile(filepath)
    # .csv  -> CsvFile(filepath)
    # .log  -> LogFile(filepath)
    # otherwise -> raise Exception("Unsupported file type: " + ext)

    # Write your code here
    if ext == ".json":
        handler = JsonFile(filepath)
    elif ext == ".csv":
        handler = CsvFile(filepath)
    elif ext == ".log":
        handler = LogFile(filepath)
    else:
        raise Exception("Unsupported file type: " + ext)


    print("=== File Handler ===")
    print("File:", filepath)
    print("Size (bytes):", handler.filesize())
    print("\n--- Content ---")
    print(handler.read())


if __name__ == "__main__":
    main()
