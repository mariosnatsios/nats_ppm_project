from src.conf import CONF
from src.actions import Actions

class LogoutPage(Actions):
    
    # ----------------------- HELPERS ------------------------
    
    def path_a_login_btn():
        """
            Returns path of 'LOGIN' button
        """
        path = "//a[@id='login']"
        return path
    
    def path_a_signup_btn():
        """
            Returns path of 'sign Up' button
        """
        path = "//a[@id='signup']"
        return path
    
    # ----------------------- CLICK ------------------------
    def click_a_login_btn(self):
        """
            Clicks the 'LOGIN' button
        """
        path = self.path_a_login_btn
        self.find_and_click(path)
        
    def click_a_login_btn(self):
        """
            Clicks the 'SignUp' button
        """
        path = self.path_a_signup_btn
        self.find_and_click(path)

    # ----------------------- VALIDATE ------------------------
    # ----------------------- SET TEXT ------------------------
    def set_text_input_email(self, text):
        """
            Sets email
        """
        path = self.path_input_email
    
    def set_text_input_password(self, text):
        """
            Sets password
        """
        path = self.path_input_password
    
    