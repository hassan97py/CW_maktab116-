import os

def copy_files_to_new_file(files_to_copy, output_file):
    with open(output_file, "w") as outfile:
        for file_path in files_to_copy:
            with open(file_path, "r") as infile:
                content = infile.read()
                outfile.write(content)
                outfile.write(" ") # Add a blank line between file contents

# Example usage
files_to_copy = ["../cw/text/file1.txt", "../cw/text/file2.txt", "../cw/text/file3.txt"]
output_file = "../cw/text/hassan.txt"

copy_files_to_new_file(files_to_copy, output_file)
print(f"Contents of the files have been copied to '{output_file}'.")





# def find_longest_sentence(x,y):
#     with open(file_pathr, 'r') as file:
#         text = file.read()

#     sentences = text.split('.')

#     longest_sentence = max(sentences, key=len)

#     word_count = len(longest_sentence.split())

#     return longest_sentence, len(longest_sentence), word_count

# file_pathr = './cw/text/file1.txt'
# file_pathr = './cw/text/file2.txt'
# file_pathr = './cw/text/file3.txt'
# longest_sentence, length, word_count = find_longest_sentence(file_pathr)
# print(f'The longest sentence is: "{longest_sentence}"')
# print(f'Length: {length} characters')
# print(f'Word count: {word_count}')

