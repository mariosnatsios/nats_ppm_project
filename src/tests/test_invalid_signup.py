import unittest
from src.fixtures import Fixtures
from src.functional import check_invalid_signup
from src.data.credentials_data import Credentials

class Test_Valid_SignUp(Fixtures):
    """
        Cheks the signup proccess
    """
    INVALID_2 = {"email": "m.natsiosdummy.com"}
    INVALID_3 = {"fullname":"mnatsios", "email": "m.natsios@dummy.com", "password": "XXX"}
    
    def test_1_check_no_data_signup(self):
        """
            Test invalid signup with no data provided
        """
        check_invalid_signup(data={})
        
    def test_2_check_invalid_email_signup(self):
        """ 
            Test invalid signup with ivalid email format
        """
        check_invalid_signup(data=self.INVALID_2, invalid_email=True)
        
    def test_3_check_existing_email_signup(self):
        """
            Test invalid signup with already existing email
        """
        check_invalid_signup(data=self.INVALID_3, existing_email=True)


if __name__ == "__main__":
    unittest.main()