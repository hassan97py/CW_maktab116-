
# def find_longest_sentence(file_path):
#     with open(file_path, 'r') as file:
#         text = file.read()
#     print(text)
#     sentences = text.split('.')

#     print(sentences)

#     lens = []

#     for f in sentences:
#         lens.append(len(f))

#     my_dict = dict(zip(sentences, lens))
#     print(my_dict)
#     # same_value_keys = [k for k, v in my_dict.items() if list(my_dict.values()).count(v) > 1]
#     same_value_keys = []

#     return same_value_keys

# file_path = './text/Q1.txt'
# same_lens = find_longest_sentence(file_path)
# print(f'Length: {same_lens} characters')

def find_longest_sentence(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    sentences = text.split('.')
    longest_sentence = max(sentences, key=len)
    length_of_longest = len(longest_sentence)
    return length_of_longest

file_path = './text/Q1.txt'
longest_sentence_length = find_longest_sentence(file_path)
print(f'Length of the longest sentence: {longest_sentence_length} characters')

