class FileReaderIterator:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(self.filename, 'r')
        self.current_line = None

    def __iter__(self):
        # self.file = open(self.filename, 'r')
        return self

    def __next__(self):
        self.current_line = self.file.readline()
        if self.current_line == '':
            self.file.close()
            raise StopIteration
        return self.current_line.strip()
    
a= r'.\cw\cw8\2\example.txt'  
b = FileReaderIterator(a)
print(b)
for line in b:
    print(line)
