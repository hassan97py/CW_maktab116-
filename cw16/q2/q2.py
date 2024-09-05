import re

class EmailValidator:
    def is_valid(self, email: str) -> bool:
        # Basic regex pattern for validating email addresses
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

# a=EmailValidator()
# print(a.is_valid('118mohammadi@gmail.com'))