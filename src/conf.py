from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class ConfigurationHelper():
    
    driver = None
    
    def set_driver(self, wd):
        
        self.driver = wd

    def set_browser(self):
        """
            Set chrome web driver
        """
        service = Service(executable_path=r'C:\Users\MariosNatsios\Downloads\chromedriver.exe')
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
        return driver
    
 # ConfigurationHelper object   
CONF = ConfigurationHelper()