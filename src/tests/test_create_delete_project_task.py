import unittest, time
from src.fixtures import Fixtures
from src.data.credentials_data import LOG_IN_CREDENTIALS
from src.functional import login, create_projects, delete_projects, \
                           create_project_task, get_project_id


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
        
        
    