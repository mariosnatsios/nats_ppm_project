import unittest, time
from src.fixtures import Fixtures
from src.data.credentials_data import LOG_IN_CREDENTIALS
from src.functional import login, edit_project_task, check_project_task


class Test_Project_Task_Update(Fixtures):
    """
        Checks the valid update/edit of a task
    """
    PROJECT_ID = "66047e6642cd4000155d7924"
    TASK_ID = "6605a06842cd4000155d797f"
    DEFAULT_DATA = {
           "summary": "Task C" ,
           "description": "A Task C", 
            "status": "TO DO",
            "labels": [],
            "file": None
        }
    
    EDIT_DATA = {
        "summary": "Task XXXX" ,
        "description": "A Task XXXX", 
        "status": "DONE",
        "labels": [],
        "file": None
    }
    
    TASKS = [
        {
            "title": "Task C" ,
            "description": "A Task C", 
            "status": "to_do",
            "labels": [],
            "file": None
        },
        
         {
            "title": "Task XXXX" ,
            "description": "A Task XXXX", 
            "status": "done",
            "labels": [],
            "file": None
        },       
        
    ]
    
    def test_1_update_task(self):
        """
            Update task
        """
        login(LOG_IN_CREDENTIALS)
        edit_project_task(task_id=self.TASK_ID, task_data=self.EDIT_DATA)
        
    def test_2_check_task(self):
        """
            Validate edited task
        """
        login(LOG_IN_CREDENTIALS)
        check_project_task(project_id=self.PROJECT_ID, task_data=self.TASKS[1])
        
    
    def test_3_reset_task(self):
        """
            Reset task
        """
        login(LOG_IN_CREDENTIALS)
        edit_project_task(task_id=self.TASK_ID, task_data=self.DEFAULT_DATA)
        
    def test_4_check_task(self):
        """
            Validate initial task
        """
        login(LOG_IN_CREDENTIALS)
        check_project_task(project_id=self.PROJECT_ID, task_data=self.TASKS[0])
    
    
    
    