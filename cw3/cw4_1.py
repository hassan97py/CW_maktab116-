
def find_longest_sentence(file_pathr):
    with open(file_pathr, 'r') as file:
        text = file.read()

    sentences = text.split('.')

    longest_sentence = max(sentences, key=len)

    word_count = len(longest_sentence.split())

    return longest_sentence, len(longest_sentence), word_count

file_pathr = '../cw/text/Q1.txt'
longest_sentence, length, word_count = find_longest_sentence(file_pathr)
print(f'The longest sentence is: "{longest_sentence}"')
print(f'Length: {length} characters')
print(f'Word count: {word_count}')

