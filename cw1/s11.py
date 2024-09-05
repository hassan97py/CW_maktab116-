str1 = 'Ynag'
str2 = 'PYnative'
flag = True
for char in str1:
    if char in str2:
        continue
    else:
        flag = False
        break

print(flag)
