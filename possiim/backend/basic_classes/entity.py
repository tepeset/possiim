from address import Address
from contact import Contact

class Entity:
    def __init__(self, classification:str, address:str, email:str, phone:int, phone_type:str, first:None, last:None, name):
        self.entity_class = classification
        self.first_name = first
        self.last_name = last
        self.get_name = name
        self.get_addresses = address
        self.get_phone = phone
        self.get_type = phone_type
        self.get_email = email

        def entity_class(self):
            try:
                if self.is_customer == True:
                    if self.is_vendor and self.is_business == False:
                        self.entityclass = "Customer"
                    else:
                        raise ValueError("Must select one entity class only.")                    
                elif self.is_vendor == True:
                    if self.is_customer and self.is_business == False:
                        self.entity_class = "Vendor"
                    else:
                        raise ValueError("Must select one entity class only.")
                elif self.is_business == True:
                    if self.is_customer and self.is_vendor == False:
                        classification == "Business"
                    else:
                        raise ValueError("Must select one entity class only.")
            finally:
                if self.is_business and self.is_vendor and self.is_customer:
                    raise ValueError("Must select one entity class only.")
                
        def is_customer(self):
            return True or not True
        def is_business(self):
            return True or not True
        def is_vendor(self):
            return True or not True
        
        def get_phone(self):
            return {self.get_phones}
        def get_email(self):
            return {self.get_emails}
        def get_type(self):
            return {self.get_phone_type}
        def get_addresses(self):
            return {self.getaddress}

        def get_name(self):
            if self.first and self.last:
                return f"{self.last}, {self.first}"
            elif self.first:
                return self.first
            elif self.last:
                return self.last
            else:
                raise ValueError("Invalid Name")
