# import os
import string
from collections import Counter  
Counter=Counter()  


def reader(file_to_open):
    with open(file_to_open, "r") as infile:
        content = infile.read()
    return content

def compare(content):
    common_words = set(content[0])
    for file_words in content[1:]:
        common_words &= set(file_words)

    num_common_words = len(common_words)

    return num_common_words, sorted(common_words)

files_to_open1 = "./text/file1.txt"
files_to_open2 = "./text/file2.txt"
files_to_open3 = "./text/file3.txt"
content = []
for file_to_open in [files_to_open1, files_to_open2, files_to_open3]:
    content.append(reader(file_to_open).lower().split())

content = [[word.strip('",.?') for word in file_words] for file_words in content]
    
# print(content.replace(string.punctuation,""))
num_common_words, common_words = compare(content)
print(f"number of the common words: {num_common_words}\n the common words: {common_words}")

