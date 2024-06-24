class Contact:
    def __init__(self, phonetype:str, number:int, email:str):
        self.phones = [{"number":number, "phone-type":phonetype}]
        self.emails = [{"email":email}]
    
        def add_phone(self, new_number:int, new_type:str):
            self.phones.append({"number":new_number, "phone-type":new_type})
        def delete_phone(self, phone_to_remove):
            self.phones = [n for n in self.phones if n["number"] != phone_to_remove]
        def get_phones(self):
            return self.phones
        def get_phone_types(self):
            return [phone["phone-type"] for phone in self.phones]
        def add_email(self, new_email:str):
            self.emails.append({"email": new_email})
        def delete_email(self, email_to_remove):
            self.emails = [n for n in self.emails if n["number"] != email_to_remove]
        def get_emails(self):
            return self.emails    
        def get_contacts(self):
            return (self.phones, self.emails)
    

        
