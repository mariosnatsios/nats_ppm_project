from src.conf import CONF
from src.actions import Actions

class LoginPage(Actions):
    
    # ----------------------- HELPERS ------------------------
    def path_input_email(self):
        """
            Return path of email input field
        """
        path = "//input[@id='email']"
        return path
    
    def path_input_password(self):
        """
            Return path of password input field
        """
        path = "//input[@id='password']"
        return path
    
    def path_button_submit(self):
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
        path = self.path_button_submit()
        self.find_and_click(path)

    # ----------------------- VALIDATE ------------------------
    def validate_p_empty_field_error_msg(self, field, msg = 'invalid login info' , exists=True):
        """
            Validate 'This field is required' error message for the mandatoty
            sign-up fields of name, email and pasword.
        """
        if field == 'email':
            path = "//form//div[contains(@class, 'row')][.//input[@id='email'][@class='invalid']] \
                        //p[contains(.,'" + str(msg) + "')]"
                        
        if field == 'password':
             path = "//form//div[contains(@class, 'row')][.//input[@id='password'][@class='invalid']] \
                    //p[contains(.,'" + str(msg) + "')]"
                    
        self.existence(path, exists=exists)
    
    # ----------------------- SET TEXT ------------------------
    def set_text_input_email(self, text):
        """
            Sets email
        """
        path = self.path_input_email()
        self.set_text(path, text)
    
    def set_text_input_password(self, text):
        """
            Sets password
        """
        path = self.path_input_password()
        self.set_text(path, text)

    
    