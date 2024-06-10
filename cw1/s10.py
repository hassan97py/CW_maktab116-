
# str = input("String : ")
str="hassa@4323ppdf%$#%"

char_count = 0
digit_count = 0
symbol_count = 0
for char in str:
    if char.isalpha():
        char_count += 1
    elif char.isdigit():
        digit_count += 1
    # if it is not letter or digit then it is special symbol
    else:
        symbol_count += 1

print("letter numbers: ", char_count)
print("digit numbers: ", digit_count)
print("symbol numbers: ", symbol_count)
