strings_list = ["apple", "banana", "Orange", "grape", "kiwi"]
chr_list = ['A']
result2 = list(filter(lambda x: x if all(c not in chr_list for c in x) else "", map(lambda i:i.upper(), strings_list)))
print(result2)