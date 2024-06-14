import string 

def is_palindrome(word):
    

    return word == word[::-1]
def p():
    for i in string.punctuation:
        # print(i)
        return i

# print(list(p()))
def find_palindromes(file_path):

    palindromes = []
    with open(file_path, 'r') as file :
        content = file.readlines()
        # print(content)
        for line in content:
            # print(line)
            for word in line.strip().split():
                word=word.lower().replace(",","")
                # print(word)
                if is_palindrome(word):
                    # print(word)
                    palindromes.append(word)
    return len(palindromes), palindromes

file_path = './text/file1.txt'
num_palindromes, palindrome_words = find_palindromes(file_path)
print("Output:")
print(f"Number of palindromic words: {num_palindromes}")
print("Words:", end=' ')
print(", ".join(f"'{word}'" for word in palindrome_words))