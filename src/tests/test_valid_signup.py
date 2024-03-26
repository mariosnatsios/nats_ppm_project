from src.fixtures import Fixtures
from src.functional import check_valid_signup
from src.data.credentials_data import Credentials

class Test_Valid_SignUp(Fixtures):
    """
        Cheks the signup proccess
    """
    CREDENTIALS = {"email": "m.natsios@dummy.com", "passoword": "1234"}
    
    
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