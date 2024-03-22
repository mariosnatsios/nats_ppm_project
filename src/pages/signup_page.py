from src.conf import CONF
from src.actions import Actions

class SignUpPage(Actions):
    
    # ----------------------- HELPERS ------------------------
    
    def path_input_fullname(self):
        
        """
            Returns path of Name input field
        """
        path = "//div[contains(@class, 'input')]//input[contains(@id, 'fullName')]"
        return path
    
    def path_input_email(self):
        
        """
            Returns path of Email input field
        """
        path = "//div[contains(@class, 'input')]//input[contains(@id, 'email')]"
        return path
    
    def path_input_password(self):
            
            """
                Returns path of Passwod input field
            """
            path = "//div[contains(@class, 'input')]//input[contains(@id, 'password')]"
            return path
    
    def path_input_company(self):
        
        """
            Returns path of Company input field
        """
        path = "//div[contains(@class, 'input')]//input[contains(@id, 'company')]"
        return path
    
    def path_input_address(self):
        
        """
            Returns path of Address input field
        """
        path = "//div[contains(@class, 'input')]//input[contains(@id, 'address')]"
        return path
    
    def path_button_sign_up(self):
        """
            Returns path of the Sign Up button
        """
        path = "//button[contains(@type, 'submit')][contains(.,'Sign Up')]"
        return path
    
    # ------------------------ CLICK --------------------------
    def click_button_sign_up(self):
        """
            Click on sign up button
        """
        path = self.path_button_sign_up()
        self.find_and_click(path)
        
        # Return the VeifyAccountPage() object
        from src.pages.verify_account import VerifyAccountPage
        return VerifyAccountPage()
    
    # ----------------------- SET TEXT ------------------------
    def set_text_input_fullname(self, firstname):
        """
            Sets name text
        """
        path = self.path_input_fullname()
        self.set_text(path, firstname)
        
    def set_text_input_email(self, email):
        """
            Sets email
        """
        path = self.path_input_email()
        self.set_text(path, email)
        
    def set_text_input_password(self, password):
        """
            Sets password
        """
        path = self.path_input_password()
        self.set_text(path, password)
        
    def set_text_input_company(self, company):
        """
            Sets company
        """
        path = self.path_input_company()
        self.set_text(path, company)
        
    def set_text_input_address(self, address):
        """
            Sets address
        """
        path = self.path_input_address()
        self.set_text(path, address)



    