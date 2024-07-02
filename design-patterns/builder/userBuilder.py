from user import User

class UserBuilder():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.address = ""
    
    @staticmethod
    def get_builder():
        return UserBuilder()
    
    def with_name(self, name):
        self.name = name
        return self
    
    def with_age(self, age):
        self.age = age
        return self

    def with_address(self, address):
        self.address = address
        return self
    
    def build(self) -> User:
        return User(self.name, 
                    self.age, 
                    self.address)