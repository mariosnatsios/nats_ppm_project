from src.conf import CONF
from src.actions import Actions

class ProjectTasksPage(Actions):
    # ----------------------- HELPERS ------------------------
    def path_div_project_task(self, status, title, descr=None, labels=[], file=None):
        """
        """
        path = "//div[contains(@id,'" + str(status) + "')]" \
                "//div[contains(@class, 'card') and @draggable]" \
                "[//span[@id='card_title'][contains(.,'" + str(title) + "')]]" 
        
        if descr:
            path += f"[//p[@id='card_description'][contains(.,'{descr}')]]"
            
        if labels:
            for label in labels:
                path += f"[//div[@id='card_label'][contains(.,'{label}')]]"
                
        if file:
            path += f"[//a[@id='card_attachments'][contains(.,'{file}')]]"
            
        return path
            
    # ----------------------- VALIDATE ------------------------
    def validate_div_project_task(self, data_to_check, exists=True):
        """
        Validate a project task
        @param data_to_check: dictionary with data for validation
        
        data_to_check = {
            "status": "to_do_items" or "in_progress_items" or "in_review_items" or "done_items",
            "title": "Task Title",
            "description": "Task Description",
            "labels": ["design", "testing"],
            "file": "images.png"
        }
        """
        path = self.path_div_project_task(status=data_to_check["status"], title=data_to_check["title"], 
                                          descr=data_to_check["description"],labels=data_to_check["labels"], 
                                          file=data_to_check["file"])
        
        self.existence(path, exists=exists)
    
    # ----------------------- CLICK ------------------------
    def click_a_edit_task(self, task_name):
        """
            Clicks Edit btn to update a task
        """
        path = "//div[@draggable][contains(.,'" + str(task_name) + "')]" \
                "//div[contains(@class, 'card-action')]//a[contains(@id, 'update_task')]"
                
        self.find_and_click(path)
    
    def click_a_delete_task(self, task_name):
        """
            Clicks Deletr btn to update a task
        """
        path = "//div[@draggable][contains(.,'" + str(task_name) + "')]" \
                "//div[contains(@class, 'card-action')]//a[contains(@id, 'delete_task')]"

        self.find_and_click(path)