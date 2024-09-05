class FileHandler:

    @classmethod
    def read_file(cls, file_path):

        try:
            with open(file_path, 'r') as file:
                contents = file.read()
            return contents
        except FileNotFoundError:
            print(f"Error: The file at '{file_path}' could not be found.")
            return None
        except IOError:
            print(f"Error: There was a problem reading the file at '{file_path}'.")
            return None
        
file_path='./cw/cw_oop/q10.txt'
a=FileHandler.read_file(file_path)
print(a)