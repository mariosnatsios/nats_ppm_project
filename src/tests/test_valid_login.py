import unittest
from src.fixtures import Fixtures
from src.functional import check_valid_login

class Test_Valid_SignUp(Fixtures):
    """
        Checks valid login
    """
    CREDENTIALS = {"email": "m.natsios@dummy.com", "password": "1234"}

    
    
    def test_1_check_login(self):
        """
            Test login with valid fullname, email and password
        """
        check_valid_login(self.CREDENTIALS)

if __name__ == "__main__":
    unittest.main()