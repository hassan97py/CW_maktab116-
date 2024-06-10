def palindrome(text):
    text2=text[::-1]
    if text==text2:
        return True
    else:
        return False
        

print(palindrome("radar"))
