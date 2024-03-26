import unittest, time
from src.fixtures import Fixtures
from src.data.credentials_data import LOG_IN_CREDENTIALS
from src.functional import login, create_projects, check_project_creation, delete_projects

class Test_Project_Creation_Deletion(Fixtures):
    """
        Checks project creation
    """
    
    ts = str(int(time.time()))
    PROJECT_NAMES = [f"Nats Project {ts}", f"Nats Project_2 {ts}"]
    PROJECTS = [{"name": PROJECT_NAMES[0], "description": f"Nats Descr {ts}"}, 
                {"name": PROJECT_NAMES[1], "description": f"Nats Descr_2 {ts}"}]
    
    def test_1_check_project_creation(self):
        """
            Create projects and validate their creation
        """
        login(LOG_IN_CREDENTIALS)
        create_projects(self.PROJECTS)
        check_project_creation(self.PROJECTS)
    
    def test_2_check_project_deletion(self):
        """
            Delete projects and validate their removal
        """
        login(LOG_IN_CREDENTIALS)
        delete_projects(self.PROJECT_NAMES)        