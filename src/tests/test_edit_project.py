import unittest, time
from src.fixtures import Fixtures
from src.data.credentials_data import LOG_IN_CREDENTIALS
from src.functional import login, create_projects,  delete_projects, get_project_id, edit_project, \
                            check_project_creation

class Test_Edit_Project(Fixtures):
    """
        Checks project creation
    """
    
    ts = str(int(time.time()))
    PROJECT_NAMES = [f"Nats Project {ts}"]
    PROJECTS = [{"name": PROJECT_NAMES[0], "description": f"Nats Descr {ts}"}]
    PROJECTS_EDITED = [{"name": f"Edited Name {ts}", "description": f"Edited Description {ts}"}]
    
    def test_1_setup(self):
        """
            Create a project
        """
        login(LOG_IN_CREDENTIALS)
        create_projects(self.PROJECTS)
        global project_id
        project_id = get_project_id(project=self.PROJECT_NAMES[0])
        
        
    def test_2_edit_project(self):
        """
            Edit the project and validate its existence in the dashboard
        """
        login(LOG_IN_CREDENTIALS)
        edit_project(project_id=project_id, input_data=self.PROJECTS_EDITED[0])
        
    def test_3_check_project(self):
        """
            Validate projectin the dashboard
        """
        login(LOG_IN_CREDENTIALS)
        check_project_creation(self.PROJECTS_EDITED)
    
    def test_4_check_reset(self):
        """
            Delete edited project
        """
        login(LOG_IN_CREDENTIALS)
        delete_projects([self.PROJECTS_EDITED[0]["name"]])    
            