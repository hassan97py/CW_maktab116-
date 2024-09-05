class EmailValueError(Exception):
    def __str__(self) -> str:
        return "email is not valid!"
class PasswordValueError(Exception):
    def __str__(self) -> str:
        return "password is not valid!"
class NameValueError(Exception):
    def __str__(self) -> str:
        return "Name is not valid!"