from address import Address
from contact import Contact

class Entity:
    def __init__(self, address:str, email:str, phone:int, phone_type:str, first:None, last:None, name):
        self.first_name = first
        self.last_name = last
        self.get_name = name
        self.get_addresses = address
        self.get_phone = phone
        self.get_type = phone_type
        self.get_email = email

        def get_phone(self):
            return [f"{self.get_phones}"]
        def get_email(self):
            return [f"{self.get_emails}"]
        def get_type(self):
            return [f"{self.get_phone_type}"]
        def get_addresses(self):
            return [f"{self.getaddress}"]

        def get_name(self):
            if self.first and self.last:
                return f"{self.last}, {self.first}"
            elif self.first:
                return self.first
            elif self.last:
                return self.last
            else:
                return "Invalid Name"