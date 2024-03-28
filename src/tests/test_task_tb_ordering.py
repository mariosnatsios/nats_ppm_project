import unittest
from src.fixtures import Fixtures
from src.data.credentials_data import LOG_IN_CREDENTIALS
from src.functional import login, check_task_db_ordering

class Test_Task_DB_Ordering(Fixtures):
    """
         Check the ordering of tasks in task DB
    """
    TASK_DEFAULT = ["Task A", "Task B", "Task C"]
    TASKS_REVERSE = ["Task C", "Task B", "Task "]
    
    def test_1_check_alphabetical(self):
        """
            Clicks the Down arrow
            Check the reverse alphabetical order tasks in task DB
            Click the down arrow
            Check the reverse alphabetical order tasks in task DB
        """
        login(LOG_IN_CREDENTIALS)
        check_task_db_ordering(task_cards_before=self.TASK_DEFAULT, 
                               task_cards_after=self.TASKS_REVERSE, arrow_direction="up")
        
        
        