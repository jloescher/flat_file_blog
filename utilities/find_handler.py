import os
from pathlib import Path


class CheckIfFileExist:
    def __init__(self, path, filename):
        super().__init__()
        self.path = path
        self.filename = filename

    def doesFileExist(self):
        filename = self.filename + ".txt"
        file = Path(self.path, filename)
        if file.is_file():
            return str(self.path) + str(filename)
        else:
            # print(file)
            return False


class FindFiles:
    def __init__(self, path, filename):
        super().__init__()
        self.path = path
        self.filename = filename

    def findFirst(self):
        for root, dirs, files in os.walk(self.path):
            for file in files:
                if file.contains(self.filename) and file.endswith(".txt"):
                    return root + "/" + str(file)


class FileNameGenerator:
    def __init__(self, filename):
        super().__init__()
        self.filename = filename

    def GenerateFilename(self):
        filename = self.filename
        filename = filename.replace(" ", "-")  # Replace spaces with dashes.
        filename = "".join(
            x for x in filename if (x.isalnum() or x in "-")
        )  # Removes all characters that are not alpha numeric or a dash.
        filename = filename.lower()

        return filename
