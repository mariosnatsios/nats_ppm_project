import unittest, time
from src.fixtures import Fixtures
from src.functional import check_invalid_project_creation, login
from src.data.credentials_data import LOG_IN_CREDENTIALS

class Test_Invalid_Project_Creation(Fixtures):
    """
        Cheks invalid project creation
    """
    ts = str(int(time.time()))
    PROJECT_NAMES = [f"Nats Project {ts}"]
    PROJECTS = [{"name": "", "description": f"Nats Descr {ts}"}, 
                {"name": PROJECT_NAMES[0], "description": ""}]
    
    def test_1_check_no_data_project_creation(self):
        """
            Test invalid project creation with no data provided
        """
        login(LOG_IN_CREDENTIALS)
        check_invalid_project_creation(project={})
    
    def test_2_check_no_name_project_creation(self):
        """ 
            Test invalid project creation with no name provided
        """
        login(LOG_IN_CREDENTIALS)
        check_invalid_project_creation(project=self.PROJECTS[0], name_error=True)
        
    def test_3_check_no_description_project_creation(self):
        """
             Test invalid project creation with no description provided
        """
        login(LOG_IN_CREDENTIALS)
        check_invalid_project_creation(project=self.PROJECTS[1], descr_error=True)
