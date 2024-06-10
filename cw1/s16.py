str1="@emma is/data*scientist%who& knows-python."
cleaned_str = ''.join(char for char in str1 if char.isalnum() or char.isspace())
# for i in str1:
#     if i.isalnum() or i.isspace():
#         c=''.join(i)
result_str = ' '.join(cleaned_str.split())  # Remove extra spaces

print(result_str)



