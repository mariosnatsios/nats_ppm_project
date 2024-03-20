from selenium import webdriver

class ConfigurationHelper():
    
    driver = None
    
    def set_driver(self, wd):
        
        self.driver = wd

    def set_browser(self):
        """
            Set chrome web driver
        """
        driver = webdriver.Chrome()
        return driver
    
 # ConfigurationHelper object   
CONF = ConfigurationHelper()