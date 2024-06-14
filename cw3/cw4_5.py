num2words1 = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
num2words2 = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
def number(Number):
    if 0 <= Number <= 19:
        return num2words1[Number]
    elif 20 <= Number <= 99:
        tens, remainder = divmod(Number, 10)
        return num2words2[tens - 2] + '-' + num2words1[remainder] if remainder else num2words2[tens - 2]
    else:
        print('Number out of implemented range of numbers.')
# print(number(8))
# def str1(n):
#     for i in n:
#         print(i)
#         if i.isdigit():
#             n=n.replace(i,number(i))
#             return n
#         else:


# input1="I have 5 dogs and 1 cat"
# # n="dfsdf"
# print(str1(input1))

# num2words = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
# 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
# 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
# 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', \
# 19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', \
# 50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', \
# 90: 'Ninety', 0: 'Zero'}

# def n2w(n):
#     try:
#         return num2words[n-n%10] + num2words[n%10].lower()
#     except KeyError:
#         print('Number out of range')

def convert(content):

    modified_content = ' '.join(number(int(word)) if word.isdigit() else word for word in content.split())
    return modified_content

# def main():
print(convert("I have 45 dogs and 1 cat."))