import unittest
from src.fixtures import Fixtures
from src.functional import check_valid_signup
from src.data.credentials_data import Credentials

class Test_Valid_SignUp(Fixtures):
    """
        Cheks the signup proccess
    """
    CREDENTIALS =  Credentials().signup_credentials()
    CREDENTIALS_OPT = Credentials().signup_credentials(optional=True)
    
    def test_1_check_signup(self):
        """
            Test signup with valid fullname, email and password
        """
        check_valid_signup(data=self.CREDENTIALS)
        
    def test_2_check_signup(self):
        """
            Test signup with valid fullname, email and password and the optional fields of
            company and address
        """
        check_valid_signup(data=self.CREDENTIALS_OPT)