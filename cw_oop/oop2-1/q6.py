class CredentialsManager:
    def __init__(self):
        self.__username = None
        self.__password = None
    
    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if not isinstance(value, str):
            raise ValueError("Username must be strings.")
        if len(value) < 3:
            raise ValueError("Username must be at least 3 characters ")
        self.__username = value

    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, value):
        if not isinstance(value, str):
            raise ValueError("password must be strings.")
        if  len(value) < 8:
                raise ValueError(" password must be at least 8 characters.")

        self.__password = value

    @username.getter
    def username(self):
        return self.__username +'23'
    
    @password.getter
    def password(self):
        return "*"*len(self.__password)

    def display_credentials(self):
        print(f"Username: {self.username}")
        print(f"Password: {self.password}")

# Example usage
credentials_manager = CredentialsManager()
credentials_manager.username="johndoe"
credentials_manager.password="hassan12"
credentials_manager.display_credentials()

