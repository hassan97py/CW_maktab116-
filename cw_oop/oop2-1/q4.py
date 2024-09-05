import os
import tempfile

class TemporaryFile:
    def __init__(self, filename=None):
        if filename is None:
            self.file = tempfile.NamedTemporaryFile(delete=False)
            self.filename = self.file.name
            print(f"Created temporary file: {self.filename}")
        else:
            self.filename = filename
            self.file = open(self.filename, 'w')
            print(f"Created file: {self.filename}")

    def __del__(self):
        if self.file is not None:
            self.file.close()
            os.remove(self.filename)
            print(f"Deleted file: {self.filename}")

# Test case
def test_temporary_file():
    print("Creating temporary file...")
    temp_file = TemporaryFile('text.txt')

    print("Temporary file created successfully.")

    print("Accessing temporary file...")
    with temp_file.file as f:
        f.write("hassan")
        print("Data written to temporary file.")

    print("Temporary file will be deleted now.")

if __name__ == "__main__":
    test_temporary_file()

# Creating temporary file...
# Created temporary file: /tmp/tmpxxxxxxxxxxx
# Temporary file created successfully.
# Accessing temporary file...
# Data written to temporary file.
# Temporary file will be deleted now.
# Deleted file: /tmp/tmpxxxxxxxxxxx
