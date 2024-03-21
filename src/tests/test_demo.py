import unittest
from src.conf import CONF
from src.fixtures import Fixtures


class Test_Demo(Fixtures):
    
    def test_1(self):
        CONF.driver.get("https://pm-tool-e63fa77e3353.herokuapp.com/")