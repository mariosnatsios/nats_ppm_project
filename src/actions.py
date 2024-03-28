from src.conf import CONF
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class Actions():
    """
        Actions Class
    """
    
    def wait_until_element_is_visible(self, target, path_type="xpath"):
        """
            Wait for element to be displayed
        """
        wait = WebDriverWait(CONF.driver, 20)

        if path_type == "xpath":
            wait.until(EC.visibility_of_element_located((By.XPATH, target)))
            
        if path_type == "css":
              wait.until(EC.visibility_of_element_located((By.CSS, target)))
        
        if path_type == "id":
              wait.until(EC.visibility_of_element_located((By.ID, target)))
              
        if path_type == "class_name":
              wait.until(EC.visibility_of_element_located((By.CLASS_NAME, target)))

        
    def wait_until_element_is_clickable(self, target, path_type="xpath"):
        """
             Wait for element to be clickable
        """
        wait = WebDriverWait(CONF.driver, 20)

        if path_type == "xpath":
            wait.until(EC.element_to_be_clickable((By.XPATH, target)))
            
        if path_type == "css":
              wait.until(EC.presence_of_alelement_to_be_clickablel_elements_located((By.CSS, target)))
        
        if path_type == "id":
              wait.until(EC.element_to_be_clickable((By.ID, target)))
              
        if path_type == "class_name":
              wait.until(EC.element_to_be_clickable((By.CLASS_NAME, target)))
              
    
    def find_and_click(self, target, path_type="xpath"):
        """
             Waits for element to be visible and then clicks it
        """
        # Wait for element to be visible and then clickable
        self.wait_until_element_is_visible(target=target, path_type=path_type)
        self.wait_until_element_is_clickable(target=target, path_type=path_type)
        
        # Define error message
        success = True
        error_msg = f"{path_type} was NOT FOUND (or is invisible) TO CLICK: {target}"
        
        
        try:
            if path_type == "xpath":
                CONF.driver.find_element(By.XPATH, target).click()
                
            if path_type == "css":
                CONF.driver.find_element(By.CSS_SELECTOR, target).click()
            
            if path_type == "id":
                    CONF.driver.find_element(By.ID, target).click()
                    
            if path_type == "class_name":
                CONF.driver.find_element(By.CLASS_NAME, target).click()
        
        except TimeoutException:
            success = False
        finally:
            assert success == True, error_msg
            
    def exists(self, target, path_type="xpath"):
        """
             Checks if element exists and is visible 
        """
        success = True
        error_msg = f"{path_type} was NOT FOUND OR IS NOT VISIBLE: {target}"
        
        try:
            self.wait_until_element_is_visible(target=target, path_type=path_type)
        except TimeoutException:
            success = False
        finally:
            assert success == True, error_msg 
            
        
    def not_exists(self, target, path_type="xpath"):
        """
            Checks if element does not exist or is visible 
        """
        success = True
        error_msg = f"{path_type} EXISTS IN DOM: {target}"
        
        if path_type == "xpath":
         found_number = len(CONF.driver.find_elements(By.XPATH, target))
        
        if found_number != 0:
            success = False
                
        if path_type == "css":
            found_number = len(CONF.driver.find_elements(By.CSS, target))
            if found_number != 0:
                success = False
                
        if path_type == "id":
            found_number = len(CONF.driver.find_elements(By.ID, target))
            if found_number != 0:
                success = False
                
        if path_type == "class_name":
            found_number = len(CONF.driver.find_elements(By.CLASS_NAME, target))
            if found_number != 0:
                success = False
                
        assert success == True, error_msg
        
    def existence(self, target, exists=True, path_type="xpath"):
        """
            uses exists or not_exists depending on 'exists'
        """

        if exists:
            self.exists(target, path_type)
        else:
            self.not_exists(target, path_type)
            
    
    def set_text(self, target, text, path_type="xpath", click=False):
        """
            Sets text to element
        """
        
        # Click the input form if neccessary
        if click:
            self.find_and_click(target, path_type=path_type)
        
        if path_type == "xpath":
            CONF.driver.find_element(By.XPATH, target).clear()
            CONF.driver.find_element(By.XPATH, target).send_keys(text)
    
        if path_type == "css":
            CONF.driver.find_element(By.CSS_SELECTOR, target).clear()
            CONF.driver.find_element(By.CSS_SELECTOR, target).send_keys(text)
            
        if path_type == "id":
            CONF.driver.find_element(By.ID, target).clear()
            CONF.driver.find_element(By.ID, target).send_keys(text)
                
        if path_type == "class_name":
            CONF.driver.find_element(By.CLASS_NAME, target).clear()
            CONF.driver.find_element(By.CLASS_NAME, target).send_keys(text)
            
    def drag_and_drop(self, from_target, to_target):
        """
            Perform drag and drop
        """
        self.exists(from_target)
        self.exists(to_target)
        
        element_from_target =  CONF.driver.find_element(By.XPATH, from_target)
        element_to_target = CONF.driver.find_element(By.XPATH, to_target)
        
        # ActionChains(CONF.driver).drag_and_drop(element_from_target, element_to_target).perform()
        
        ActionChains(CONF.driver).click_and_hold(element_from_target).move_to_element(element_to_target).release(element_to_target).perform()


            
            
            

        