
class FileInputter:
    # Constants:
    allowedFileTypes = [".cpp", ".c", ".py", ".java"] #accepted cource code file types

    # Constructor: takes in fileName and gets extension for fileName
    def __init__(self, fileName):
        self.fileName = fileName
        self.fileExtension = r""
        getExtension = False

        for c in self.fileName:
            if (getExtension == True):
                self.fileExtension += c
            if (c == "."):
                getExtension = True
                self.fileExtension += c

    # Function: Checks to see if the provided file's extension is valid
    def checkFile(self):
        for c in self.allowedFileTypes:
            if (self.fileExtension == c):
                return True

        return False

    # Function: reads a single line from the file
    def readFile(self):
        self.fileContents = []
        try:
            self.fileObject = open(self.fileName, "r")
        except FileNotFoundError:
            print("File does not exist in scope")
            return

        for line in self.fileObject:
            line = line.strip()

            if (not line.startswith('#')):
                self.fileContents.append(line)

        self.fileObject.close()
        return self.fileContents
