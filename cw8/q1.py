import re

class TextFormatter:
    def replace_dates(self, text):
    # """
    # Replaces dates in the format DD/MM/YYYY with YYYY-MM-DD
    # """
        return re.sub(r'(\d{2})/(\d{2})/(\d{4})', r'\3-\2-\1', text)

    def find_all_urls(self, text):
    # """
    # Finds all URLs in the given text
    # """
        return re.findall(r'https?://\S+', text)

# Sample text
text = "My birthday is 25/12/1990. Check out this website: https://www.example.com and this one: http://another.com"

formatter = TextFormatter()
print(formatter.replace_dates(text))
# Output: My birthday is 1990-12-25. Check out this website: https://www.example.com and this one: http://another.com

print(formatter.find_all_urls(text))
# Output: ['https://www.example.com', 'http://another.com']