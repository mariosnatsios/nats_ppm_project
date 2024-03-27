from src.conf import CONF
from src.actions import Actions

class CreateProjectPage(Actions):
    
     # ----------------------- HELPERS ------------------------
    
    def path_input_name(self):
        
        """
            Returns path of Name input field
        """
        path = "//div[contains(@class, 'input')]//input[contains(@id, 'name')]"
        return path
    
    def path_input_description(self):
        
        """
            Returns path of Description input field
        """
        path = "//div[contains(@class, 'input')]//input[contains(@id, 'description')]"
        return path
    
    # -----------------------VALIDATE ------------------------
    def validate_p_name_requird_error_msg(self,  msg = 'This field is required' , exists=True):
        """
            Validate the 'This field is required' for name field
        """
        path = "//form//div[contains(@class, 'row')][.//input[@id='name'][@class='invalid']] \
                     //p[contains(.,'" + str(msg) + "')]"
                    
        self.existence(path, exists=exists)
        
    def validate_p_description_requird_error_msg(self,  msg = 'This field is required' , exists=True):
        """
             Validate the 'This field is required' for description field
        """
        path = "//form//div[contains(@class, 'row')][.//input[@id='description'][@class='invalid']] \
                     //p[contains(.,'" + str(msg) + "')]"
                    
        self.existence(path, exists=exists)
        
    def validate_p_empty_field_error_msg(self, field, msg = 'This field is required' , exists=True):
        """
            Validate 'This field is required' error message for the mandatoty
            sign-up fields of name, email and pasword.
        """
        if field == 'name':
            path = "//form//div[contains(@class, 'row')][.//input[@id='name'][@class='invalid']] \
                     //p[contains(.,'" + str(msg) + "')]"
                     
        if field == 'description':
            path = "//form//div[contains(@class, 'row')][.//input[@id='description'][@class='invalid']] \
                        //p[contains(.,'" + str(msg) + "')]"
                        
        self.existence(path, exists=exists) 


     # ----------------------- CLICK -------------------------

    def click_button_create(self):
        """
            Clicks the 'CREATE' button
        """
        path = "//button[@type='submit'][contains(.,'Create')]"
        self.find_and_click(path)
    
     # ----------------------- SET TEXT ------------------------
    def set_text_input_name(self, name):
        """
            Sets project name text
        """
        path = self.path_input_name()
        self.set_text(path, name)
        
    def set_text_input_description(self, descr):
        """
            Sets description
        """
        path = self.path_input_description()
        self.set_text(path, descr)
    