import re
class Validator:
    @classmethod
    def check_email(cls, email):
        valid = r'\b[A-Za-z0-9._]+@[A-Za-z]+\.[A-Z|a-z]{2,7}\b'

        if(re.fullmatch(valid, email)):
            return True
        else:
            return False
        
    def check_password(cls , password):
        valid=r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
        if(re.fullmatch(valid, password)):
            return True
        else:
            return False
        
email = "ankitrai326@gmail.com"
Validator.check(email)

email = "my.ownsite@our-earth.org"
Validator.check(email)

email = "ankitrai326.com"
Validator.check(email)

email = "ankitrai326@aaa.comsadaa"
Validator.check(email)