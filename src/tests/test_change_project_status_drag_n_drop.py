import unittest, time
from src.fixtures import Fixtures
from src.data.credentials_data import LOG_IN_CREDENTIALS
from src.functional import login, change_project_task_status, check_project_task


class Test_Change_Project_Task_Status_Drag_N_Drop(Fixtures):
    """
    """
    DATA = {
        
        "status_from": "to_do",
        "status_to": "in_progress",
        "title": "Task A",
        "project_id": "66047e6642cd4000155d7924",
        
    }
        
    DATA_RESET = {
        "status_from": "in_progress",
        "status_to": "to_do",
        "title": "Task A",
        "project_id": "66047e6642cd4000155d7924"}
        
    
    
    TASKS = [
        {
            "status": "in_progress",
            "title": "Task A",
            "description": "A simple task",
            "labels": [],
            "file": None
            
        },
        
        {
            "status": "to_do",
            "title": "Task A",
            "description": "A simple task",
            "labels": [],
            "file": None
        }
        
        ]
        
    
    def test_1_project_status_change(self):
        """
            Move task TO DO -----> IN PROGRESS status
        """
        login(LOG_IN_CREDENTIALS)
        change_project_task_status(project_id=self.DATA["project_id"], title=self.DATA["title"], 
                                   status_from=self.DATA["status_from"], 
                                   status_to=self.DATA["status_to"])
        
        
    def test_2_check_project_task_status(self):
        """
            Check new status for task
        """
        login(LOG_IN_CREDENTIALS)
        check_project_task(project_id=self.DATA["project_id"], task_data=self.TASKS[0])

        
        
    def test_3_project_status_reset(self):
        """
          Reset status IN PROGRESS -----> TO DO
        """
        login(LOG_IN_CREDENTIALS)
        change_project_task_status(project_id=self.DATA_RESET["project_id"], title=self.DATA_RESET["title"], 
                                   status_from=self.DATA_RESET["status_from"], 
                                   status_to=self.DATA_RESET["status_to"])
        
        
    def test_4_check_project_task_status(self):
        """
            Check initial status for task
        """
        login(LOG_IN_CREDENTIALS)
        check_project_task(project_id=self.DATA["project_id"], task_data=self.TASKS[1])

    
if __name__ == "__main__":
    unittest.main()