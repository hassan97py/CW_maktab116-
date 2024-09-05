class FileWriter:

    @classmethod
    def write_to_file(cls, file_path,data):

        with open(file_path, 'a') as file:
            file.write(data)
 
data='mohammadi'       
file_path='./cw/cw_oop/q10.txt'
FileWriter.write_to_file(file_path,data)
