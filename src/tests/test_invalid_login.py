import unittest
from src.fixtures import Fixtures
from src.functional import check_invalid_login

class Test_Valid_SignUp(Fixtures):
    """
        Checks valid login
    """
    
    def test_1_check_no_data_invalid_login(self):
        """
            Test invalid login with no data
        """
        check_invalid_login(data={})
        
        
    def test_2_check_no_email_invalid_login(self):   
        """
            Test invalid login with no email
        """
        check_invalid_login(data={"password": "CCC"}, error_fields=['email'])
        
        
    def test_3_check_no_password_invalid_login(self):   
        """
            Test invalid login with no email
        """
        check_invalid_login(data={"email": "mmm@example.com"}, error_fields=['password'])
        