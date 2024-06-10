str1="hasss12 hhh hbh mohammadi65 fgh fcf"
import re
words = str1.split()
# res = [word for word in words if words.isalnum() and words.isalpha() and words.isdigit()]
for i in words:
    if i.isalpha() and i.isalnum() :
        print(i)

