class FileReader:
    def __init__(self, filename,mode='r'):
        self.mode=mode
        self.filename = filename
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
        if exc_type is not None:
            print(f"An error occurred: {exc_value}")
            traceback.print_tb(traceback)
        return True
    
with FileReader(r'.\cw\cw8\2\example.txt','r') as file:
    content = file.read()
    print(content)
# with open()