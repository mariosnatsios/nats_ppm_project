from src.conf import CONF
import unittest

class Fixtures(unittest.TestCase):
    """
        Setup/Teardown before each test case
    """
    def setUp(self):
        # Set webdriver before each test case
        self.wd = CONF.set_browser()
        CONF.set_driver(self.wd)
        CONF.driver.implicitly_wait(5)
    
    def tearDown(self):
        # Quit webdriver before each test case
        self.wd.quit()
