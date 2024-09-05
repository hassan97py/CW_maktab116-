
# class StringUtils:
#     def reverse(self, text):
#         return text[::-1]

#     def capitalize(self, text):
#         return text.capitalize()

#     def count_words(self, text):
#         return len(text.split())

class StringUtils:
    @staticmethod
    def reverse(s):
        return s[::-1]

    @staticmethod
    def count_words(s):
        return len(s.split())

    @staticmethod
    def capitalize(s):
        return s.capitalize()
