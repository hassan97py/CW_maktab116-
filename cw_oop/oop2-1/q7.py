# from email import Validator
# D:\maktab116\amir_reza_tehrani\HW3\aaaa.py

from amir_reza_tehrani.HW3.aaaa import Validator
from exception import EmailValueError,PasswordValueError

class EmailAccount:
    def __init__(self) -> None:
        self.__email_address=None
        self.__password=None

    @property
    def email_address(self):
        return self.__email_address
    @email_address.setter
    def email_address(self,value):
        if Validator.check_email(value):
            self.__email_address=value
        else:
            raise EmailValueError 
        
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self,value):
        if Validator.check_password(value):
            self.__password=value
        else:
            raise PasswordValueError

    
    @password.getter
    def password(self):
        return ":)"*len(self.__password)
    
    def display(self):
        print(f"Username: {self.email_address}")
        print(f"Password: {self.password}")

hassan=EmailAccount()
hassan.email_address='118mohammadi@gmail.com'   
hassan.password='1234@hhH123'
hassan.display()
# amir=EmailAccount('118mohammadi@gmail.com','1234@hhH123')
# amir.email_address='3213@dffds'
# amir.password='32333'
# amir.display()