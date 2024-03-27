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
     
    # ----------------------- CLICK ------------------------
    def click_a_create_project_btn(self):
        """
            Clicks the "Create" button to create a new project
        """
        path = "//a[contains(.,'Create')]"
        self.find_and_click(path)
        # Return the new page (createProject) after the click
        from src.pages.create_project import CreateProjectPage
        create_project_page = CreateProjectPage()
        return create_project_page
    
    def click_a_delete_project(self, project):
        """
            Delete a project
        """
        path = "//div[contains(@class, 'card')][.//span[contains(.,'" + str(project) + "')]] \
                //a[contains(@id, 'delete_project')]"
        self.find_and_click(path)
        
    # ----------------------- VALIDATE ------------------------
    def validate_span_welcome_card_title(self, exists=True):
        """
            Validates path of welcome card title
        """
        path =  self.path_span_welcome_card_tilte()
        self.existence(path, exists=exists)
    
    def validate_div_project_name(self, title, exists=True):
        """
            Validate a project exists (or not) in dashboard, based on title
        """
        path = "//div[contains(@class, 'card-content')][.//span[contains(.,'" + str(title) + "')]]"
        
        self.existence(path, exists=exists)
        
    def validate_div_project(self, title, descr, exists=True):
        """
            Validate a project exists (or not) in dashboard, based on its title and description
        """
        path = "//div[contains(@class, 'card-content')][.//span[contains(.,'" + str(title) + "')]] \
               [contains(.,'" + str(descr) + "')]"
        
        self.existence(path, exists=exists)
        
    def validate_a_create_project_btn(self, exists=True):
        """
            Validates the "Create" button 
        """
        path = "//a[contains(.,'Create')]"
        self.existence(path, exists=exists)
     
