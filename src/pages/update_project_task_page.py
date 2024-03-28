from src.pages.create_task_page import CreateTaskPage

class UpdateTaskPage(CreateTaskPage):
    # ----------------------- HELPERS ------------------------
    def path_button_update_task_button(self):
        """
            Returns path of Update button
        """
        path = "//button[@type='submit'][contains(.,'Update')]"
        return path
    
    # ----------------------- CLICK --------------------------
    def click_button_update_task(self):
        """
            Clicks the Update button
        """
        path = self.path_button_update_task_button()
        self.find_and_click(path)