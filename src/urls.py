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
    
    def home_page(self):
        """
            Navigate to homepage
        """
        from src.pages.home_page import HomePage
        url = "https://pm-tool-e63fa77e3353.herokuapp.com/dashboard"
        CONF.driver.get(url)
        # Return page object
        return HomePage()
    
    def logout_page(self):
        """
            Login Page
        """
        from src.pages.logout_page import LogoutPage
        
        url = "https://pm-tool-e63fa77e3353.herokuapp.com/logout"
        CONF.driver.get(url)
        # Return page object
        return LogoutPage()
    
    def signup_page(self):
        """
            Signup Page
        """
        from src.pages.signup_page import SignUpPage
        
        url = "https://pm-tool-e63fa77e3353.herokuapp.com/signup"
        CONF.driver.get(url)
        # Return page object
        return SignUpPage()

    def create_project_page(self):
        """
            Navigates to createProject page
        """
        from src.pages.create_project import CreateProjectPage
        url = "https://pm-tool-e63fa77e3353.herokuapp.com/createProject"
        CONF.driver.get(url)
        # Return page object
        return CreateProjectPage()
    
    def edit_project(self, project_id):
        """
            Navigates to update project page for a specific project id 
        """
        from src.pages.update_project_page import UpdateProjectPage
        
        url = f"https://pm-tool-e63fa77e3353.herokuapp.com/projects/{project_id}/update"
        CONF.driver.get(url)
        # Return page object
        return UpdateProjectPage()
    
    
    def create_task_page(self, project_id):
        """
            Navigates to create task page for a specific project id 
        """
        from src.pages.create_task_page import CreateTaskPage
        
        url = f"https://pm-tool-e63fa77e3353.herokuapp.com/projects/{project_id}/createTask"
        CONF.driver.get(url)
        # Return page object
        return CreateTaskPage()
    
    def project_tasks_page(self, id):
        """
               Navigates to project tasks page for a specific project id 
        """
        from src.pages.project_tasks_page import ProjectTasksPage
        url = f"https://pm-tool-e63fa77e3353.herokuapp.com/projects/{id}/tasks"
        CONF.driver.get(url)
        # Return page object
        return ProjectTasksPage()
    
    def update_tasks_page(self, id):
        """
            Navigates to update task page for a specific task id
        """
        from src.pages.update_project_task_page import UpdateTaskPage
        url = f"https://pm-tool-e63fa77e3353.herokuapp.com/tasks/{id}/update"
        CONF.driver.get(url)
        # Return page object
        return UpdateTaskPage()
    
    def tasks_db_page(self):
        """
            Navigates to task db page
        """
        from src.pages.tasks_db_page import TaskDbPage
        url = "https://pm-tool-e63fa77e3353.herokuapp.com/tasks/db"
        CONF.driver.get(url)
        # Return page object
        return TaskDbPage()
        
    
        
        

    