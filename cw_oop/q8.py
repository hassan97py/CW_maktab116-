import re
class Validator:
    @classmethod
    def check(cls, email):
        valid = r'\b[A-Za-z0-9._]+@[A-Za-z]+\.[A-Z|a-z]{2,7}\b'

        if(re.fullmatch(valid, email)):
            print("Valid Email")

        else:
            print("Invalid Email")

email = "ankitrai326@gmail.com"
Validator.check(email)

email = "my.ownsite@our-earth.org"
Validator.check(email)

email = "ankitrai326.com"
Validator.check(email)

email = "ankitrai326@aaa.comsadaa"
Validator.check(email)