from src.conf import CONF
from src.actions import Actions

class UpdateProjectPage(Actions):
    
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
    
     # ----------------------- CLICK -------------------------

    def click_button_update(self):
        """
            Clicks the 'UPDATE' button
        """
        path = "//button[@type='submit'][contains(.,'Update')]"
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
    