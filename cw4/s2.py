
def count_vowels(s):
    return sum(1 for c in s.lower() if c in 'aeiou')

my_list = ["apple", "banana", "cherry", "date", "elderberry"]
sorted_list = sorted(my_list, key=lambda x: count_vowels(x), reverse=True)

print(sorted_list)