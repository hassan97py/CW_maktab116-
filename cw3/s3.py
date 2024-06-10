# def string_test(str1):
#     u=0
#     l=0
#     for i in str1:
#         if i.isupper():
#             u+=1
#         elif i.islower():
#             l+=1
#         else:
#             pass
#     print("letters upper:",u)    
#     print("letters lower",l)   

# string_test("dfsdfdsfFGFDSGSG")


def string_test(s,d):
    for i in s:
        if i.isupper():
           d["UPPER_CASE"] += 1
        elif i.islower():
           d["LOWER_CASE"] += 1
        else:
          pass

d = {"UPPER_CASE": 0, "LOWER_CASE": 0}
s = 'The quick Brown Fox'
string_test(s,d)
print("Original String: ", s)
print("No. of Upper case characters: ", d["UPPER_CASE"])
print("No. of Lower case Characters: ", d["LOWER_CASE"])