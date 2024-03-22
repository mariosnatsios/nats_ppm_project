from src.fixtures import Fixtures
from src.functional import check_valid_signup
from src.data.credentials_data import signup_credentials

class Test_Valid_SignUp(Fixtures):
    """
        Cheks the signup proccess
    """
    CREDENTIALS = signup_credentials()
    
    def test_check_signup(self):
        """
        """
        check_valid_signup(data=self.CREDENTIALS)