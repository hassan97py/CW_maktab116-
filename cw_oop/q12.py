class StringUtil:
    @classmethod
    def reverse_string(cls, input_string):

        return input_string[::-1]
    
# original_string = "Hello, World!"
# reversed_string = StringUtil.reverse_string(original_string)
# print(reversed_string) 
print(StringUtil.reverse_string(input(':')))