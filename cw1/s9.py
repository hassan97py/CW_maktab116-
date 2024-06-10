
str1 = input("string 1 :")
str2 = input("string 2 :")

sizestr1 = len(str1)

a = sizestr1 // 2

str3 = str1[:a]+str2+str1[a:]

print(str3)