from random import randint



class Credentials():
    """
        Generate/Store credentials for signup and login
    """
    def __init__(self):
         self.ts = str(randint(1111111,2222222))
    

    def signup_credentials(self, optional=False):
        """
            Returns  dictionaty with valid signup credentials 
        """
            
        credentials = {
            "fullname": "DummyName" + self.ts,
            "password": "DummyPassword" + self.ts,
            "email": f"dummy{self.ts}@example.com",
            "company": "",
            "address": ""
        }
        # If we want the optianal credentials of company and address to be included in the signup form
        if optional:
            credentials.update({ "company": f"DummyCompany{self.ts}",  "address": f"DummyAddress{self.ts}"})
        
        return credentials