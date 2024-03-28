from src.actions import Actions

class CreateTaskPage(Actions):
     # ----------------------- HELPERS ------------------------
    
    def path_input_summary(self):
        
        """
            Returns path of Summary input field
        """
        path = "//div[contains(@class, 'input')]//input[contains(@id, 'summary')]"
        return path
    
    def path_textarea_description(self):
        
        """
            Returns path of Description textarea field
        """
        path = "//div[contains(@class, 'input')]//textarea[contains(@id, 'description')]"
        return path
    
    def path_input_status_dropdown(self):
        """
            Returns path of status dropdown
        """
        path = "//div[contains(@class, 'input-field')][contains(.,'Status')]//input"
        return path
    
    def path_li_status_dropdown_option(self, option):
        """
            Returns path of specific list option from the status dropdown
        """
        path = "//div[contains(@class, 'input-field')][contains(.,'Status')]//li[contains(.,'" + str(option) + "')]"
        return path
    
    def path_input_labels_dropdown(self):
        """
            Returns path of labels dropdown
        """
        path = "//div[contains(@class, 'input-field')][contains(.,'Labels')]//input"
        return path
    
    def path_li_labels_dropdown_option(self, option):
        """
            Returns path of specific list option from the labels dropdown
        """
        path = "//div[contains(@class, 'input-field')][contains(.,'Labels')]//li[contains(.,'" + str(option) + "')]"
        return path
    
    def path_button_create_task_button(self):
        """
            Returns path of Create button
        """
        path = "//button[@type='submit'][contains(.,'Create')]"
        return path
    
    def path_input_upload_file(self):
        """
            Returns path of upload file input field
        """
        path = "//input[@id='attachments']"
        return path
    
    def find_input_attachement_field(self):
        """
            Finds the input field fot attachment uploading
        """
        input_obj = self.find_element(self.path_input_upload_file())
        return input_obj

    # ----------------------- CLICK --------------------------
    def click_li_status_dropdown_option(self, option):
        """
            Opens Status option and clicks/selects a list option
        """
        path_1 = self.path_input_status_dropdown()
        self.find_and_click(path_1)
        path_2 = self.path_li_status_dropdown_option(option)
        self.find_and_click(path_2)
       
    def click_li_labels_dropdown_option(self, option):
        """
            Opens Labels option and clicks/selects a list option
        """
        path_1 = self.path_input_labels_dropdown()
        self.find_and_click(path_1)
        path_2 = self.path_li_labels_dropdown_option(option)
        self.find_and_click(path_2)
        
    def click_button_create_task(self):
        """
            Clicks the Create button
        """
        path = self.path_button_create_task_button()
        self.find_and_click(path)
                            
    # ----------------------- SET-TEXT ------------------------
    def set_text_input_summary(self, text):
        
        """
            Sets Summary
        """
        path = self.path_input_summary()
        self.set_text(path, text)
        
    def set_text_input_description(self, text):
        
        """
            Sets Description
        """
        path = self.path_textarea_description()
        self.set_text(path, text)
 
    
    
    
        