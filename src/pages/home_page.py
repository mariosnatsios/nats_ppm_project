from src.conf import CONF
from src.actions import Actions

class HomePage(Actions):
    # ----------------------- HELPERS ------------------------
    def path_span_welcome_card_tilte(self):
         """
            Returns path of welcome card title
         """
         path = "//div[contains(@class,'card-content')]//span[contains(.,'Welcome')]"
         return path
     
    # ----------------------- VALIDATE ------------------------
    def validate_span_welcome_card_title(self, exists=True):
        """
            Validates path of welcome card title
        """
        path =  self.path_span_welcome_card_tilte()
        self.existence(path, exists=exists)
     
