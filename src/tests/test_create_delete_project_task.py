import unittest, time
from src.fixtures import Fixtures
from src.data.credentials_data import LOG_IN_CREDENTIALS
from src.functional import login, create_projects, delete_projects, \
                           create_project_task, get_project_id, \
                           check_project_task, delete_project_task 


class Test_Create_Delete_Project_Task(Fixtures):
    """
        Checks project task creation
    """
    ts = str(int(time.time()))
    PROJECT_NAMES = [f"Nats Project {ts}"]
    PROJECTS = [{"name": PROJECT_NAMES[0], "description": f"Nats Descr {ts}"}]
    
    TASKS = [
        {
           "summary": f"Project Task Summary {ts}" ,
           "description": f"Project Task Description {ts}", 
            "status": "IN PROGRESS",
            "labels": ["design", "testing"],
            "file": "images.jpg"
        }
    ]
    
    TASK_TO_CHECK = {
           "title": f"Project Task Summary {ts}" ,
           "description": f"Project Task Description {ts}", 
            "status": "in_progress",
            "labels": ["design", "testing"],
            "file": "images.jpg"
        }

    def test_1_setup(self):
            """
                Create a project
            """
            login(LOG_IN_CREDENTIALS)
            create_projects(self.PROJECTS)
            global project_id
            project_id = get_project_id(project=self.PROJECT_NAMES[0])
            
    def test_2_create_task(self):
        """
            Create task for the created project
        """
        login(LOG_IN_CREDENTIALS)
        create_project_task(project_id, self.TASKS[0])
        
    def test_3_check_task(self):
        """
            Validate created task in project tasks
        """
        login(LOG_IN_CREDENTIALS)
        check_project_task(project_id=project_id, task_data=self.TASK_TO_CHECK)
        
    def test_4_delete_task(self):
        """
            Delete created task
        """
        login(LOG_IN_CREDENTIALS)
        delete_project_task(project_id=project_id, task_names=[self.TASK_TO_CHECK["title"]])
        
    def test_5_check_task(self):
        """
            Check deleted task removal
        """
        login(LOG_IN_CREDENTIALS)
        check_project_task(project_id=project_id, task_data=self.TASK_TO_CHECK, exists=False)
        
        
    def test_6_delete_project(self):
        """
            Delete created project and reset
        """
        login(LOG_IN_CREDENTIALS)
        delete_projects(self.PROJECT_NAMES)
        
    