class User():
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def set_name(self, name: str):
        self.name = name

    def get_name(self):
        return self.name
    
    def set_age(self, age: int):
        self.age = age

    def get_age(self):
        return self.age
    
    def set_address(self, address: str):
        self.address = address

    def get_address(self):
        return self.address
    
    def print_user(self):
        print(f"name - {self.name}")
        print(f"age - {self.age}")
        print(f"address - {self.address}")