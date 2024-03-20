from src.conf import CONF
from src.actions import Actions

class LoginPage(Actions):
    
    # ----------------------- HELPERS ------------------------
    def path_input_email():
        """
            Return path of email input field
        """
        path = "//input[@id='email']"
        return path
    
    def path_input_password():
        """
            Return path of password input field
        """
        path = "//input[@id='password']"
        return path
    
    def path_button_submit():
        """
            Returns path of 'LOGIN' button
        """
        path = "//button[@type='submit']"
        return path
    
    # ----------------------- CLICK ------------------------
    def click_button_submit(self):
        """
            Clicks the 'LOGIN' button
        """
        path = self.path_button_submit
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
    
    
    