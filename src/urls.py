from src.conf import CONF

class Navigate():
    """
          Different page navigations
    """
    
    def login_page(self):
        """
            Login Page
        """
        from src.pages.login_page import LoginPage
        
        url = "https://pm-tool-e63fa77e3353.herokuapp.com/login"
        CONF.driver.get(url)
        # Return page object
        return LoginPage()
        