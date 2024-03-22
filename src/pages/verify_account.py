from src.conf import CONF
from src.actions import Actions

class VerifyAccountPage(Actions):
    
    # ------------------ VALIDATE ---------------------
    def validate_span_verify_account_card(self, exists=True):
        """
            Check the existence of 'Verify your accout' card in page
        """
        path = " //div[contains(@class,'card')]//span[contains(.,'Verify your account')]"
        self.existence(path, exists=exists)