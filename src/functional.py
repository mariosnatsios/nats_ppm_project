import time
from src.urls import Navigate
from src.conf import CONF
navigate = Navigate()

def signup(data):
    """
        Fills the sign up form 
        @param data: dictionary with the field categories and data for the various fields to be populated.
        
        data = {
            "fullname": "John Sick",
            "email": "j.sick@giant.com",
            "passoword": "XXXX",
            "company": "Giant",
            "address": "Forse 2 Crypton"
        }
    """
    page = navigate.signup_page()
    
    if "fullname" in data.keys():
        page.set_text_input_fullname(data["fullname"])
    
    if "email" in data.keys():
        page.set_text_input_email(data["email"])
        
    if "password" in data.keys():
        page.set_text_input_password(data["password"])
        
    if "company" in data.keys():
        page.set_text_input_company(data["company"])
        
    if "address" in data.keys():
        page.set_text_input_address(data["address"])
        
    # Clicks the Sign Up button
    confirmation_page = page.click_button_sign_up()
    # Return confirmation page object for furher validation if neccessary
    return confirmation_page
    
    
def check_valid_signup(data):
    """
         Fills the sign up form
         Checks successfull signup
        @param data: dictionary with the field categories and data for the various fields to be populated.
        
        data = {
            "fullname": "John Sick",
            "email": "j.sick@giant.com",
            "passoword": "XXXX",
            "company": "Giant",
            "address": "Forse 2 Crypton"
        }
    """
    # Perform the signup
    account_verifiacation_page = signup(data)
    
    # Verify the account confirmation page
    account_verifiacation_page.validate_span_verify_account_card()
     # Validate current url
    current_url = CONF.driver.current_url
    assert current_url == "https://pm-tool-e63fa77e3353.herokuapp.com/verifyAccount", "NOT THE CORRECT LANDING PAGE!!"
    
    
def check_invalid_signup(data, invalid_email=False, existing_email=False):
    """
        Checks invalid signup
         @param data: dictionary with the field categories and data for the various fields to be populated.
        
        data = {
            "fullname": "John Sick",
            "email": "j.sick@giant.com",
            "passoword": "XXXX",
            "company": "Giant",
            "address": "Forse 2 Crypton"
        }
        
        @param error_fields: lists of the field names we want to check for error --> ['name', 'email', 'password']
    """
    from src.pages.signup_page import SignUpPage
    signup_page = SignUpPage()
    # Perform SignUp
    signup(data)
    
    if not data:
        error_fields =  ['name', 'email', 'password']
        # Validate error message 'This field is required' appears for all name, email and password fields
        for field in error_fields:
            signup_page.validate_p_empty_field_error_msg(field)
    else:
        # Check invalid email format error message       
        if invalid_email:
            signup_page.validate_p_invalid_email_error_msg()
        # Check already existing email error message
        if existing_email:
            signup_page.validate_p_already_exist_email_error_msg(email=data["email"])
        
     # Validate current url
    current_url = CONF.driver.current_url
    assert current_url == "https://pm-tool-e63fa77e3353.herokuapp.com/signup", "NOT THE CORRECT LANDING PAGE!!"
    

def login(data):
    """
        Performs login
         
          @param data: dictionary with the field categories and data for the various fields to be populated.
        
        data = {
            "email": "j.sick@giant.com",
            "passoword": "XXXX",
        }
    """
    page = navigate.login_page()
    
    if "email" in data.keys():
        page.set_text_input_email(data["email"])
        
    if "password" in data.keys():
        page.set_text_input_password(data["password"])
        
     # Clicks the Login button
    page.click_button_submit()
    time.sleep(2)
    
        
def check_valid_login(data):
    """
         Fills the login form
         Checks successfull login
         
          @param data: dictionary with the field categories and data for the various fields to be populated.
        
        data = {
            "email": "j.sick@giant.com",
            "passoword": "XXXX",
        }
    """
    from src.pages.home_page import HomePage
    home_page =  HomePage()
    # Perform Login
    login(data)
    # Validate Welcome card
    home_page.validate_a_create_project_btn()
    # Validate homepage/dashboard url
    current_url = CONF.driver.current_url
    assert current_url == "https://pm-tool-e63fa77e3353.herokuapp.com/dashboard", "NOT THE CORRECT LANDING PAGE!!"
    
def check_invalid_login(data, error_fields = []):
    """
        Checks invalid login
        @param error fields: Lists of field name with error to be checke --> ['email', 'password']
        @param data: dictionary with the field categories and data for the various fields to be populated.
        
        data = {
            "email": "j.sick@giant.com",
            "passoword": "XXXX",
        }
    """
    from src.pages.login_page import LoginPage
    login_page = LoginPage()
    
    # Perform login
    login(data)
    
    if not data:
        error_fields =  ['email', 'password']
        # Validate error message 'This field is required' appears for all email and password fields
        for field in error_fields:
            login_page.validate_p_empty_field_error_msg(field)
    else:
        # Use the user input for specific error fields you want to check
        for field in error_fields:
            login_page.validate_p_empty_field_error_msg(field)
            
    # Validate that the current url is still the one of the login page
    current_url = CONF.driver.current_url
    assert current_url == "https://pm-tool-e63fa77e3353.herokuapp.com/login", "WRONG LANDING PAGE!!"
    
def get_project_id(project):
    """
        Retrieve the id of a newly created project from the url
        @param project: name of project the name of which we want to retrieve
    """
    page = navigate.home_page()
    # Click the Edit button
    page.click_a_edit_project(project)
    # Retrieve project id
    current_url= CONF.driver.current_url
    project_id = current_url.split("/")[4]
    return project_id
    
def create_projects(projects):
    """
        Fills the create project form and creates a project by clicking the corresponding button
        
         @param projects: list of dictionaries with the field categories and data for the various fields to be populated.
        
        projects = 
        [
            {
            "name": "My_ProJect_Name",
            "description": "A project description",
            }
        ]
    """
    
    for project in projects:
        # navigate to create project page
        page = navigate.create_project_page()
        
        if "name" in project.keys():
            page.set_text_input_name(project["name"])
        
        if "description" in project.keys():
            page.set_text_input_description(project["description"])
        # Click the create button
        page.click_button_create()
    
def check_project_creation(projects, exists=True):
    """
        @param projects: list of dictionaries with project names and
                     their corresponding descriptions to check
        
        projects = [ {
            "name": "My_ProJect_Name",
            "description": "A project description",
            },
            
            {
            "name": "My_ProJect_Name_2",
            "description": "A project description_2",
            },  
            
            ]
    """
    # Go to Dashboard
    page = navigate.home_page()
    # Validate the existing projects
    for project in projects:
        page.validate_div_project(title=project["name"], descr=project["description"], 
                                  exists=exists)
        
def delete_projects(projects):
    """
        Delete projects bases on titlte
        @param project: list of project names we want to delete
    """
     # Go to Dashboard
    page = navigate.home_page()
    time.sleep(2)
    for project in projects:
        page.click_a_delete_project(project)
        CONF.driver.switch_to.alert.accept()
        time.sleep(1)
        # Refresh and validate the successful deletion
        CONF.driver.refresh()
        page.validate_div_project_name(project, exists=False)
        
        
def check_invalid_project_creation(project, name_error=False, descr_error=False):
    """
     @param projects: dictionary with the field categories and data for the various fields to be populated.
        
        projects = 
        [
            {
            "name": "My_ProJect_Name",
            "description": "A project description",
            },
            ...
            {
                ...
            }
        ]
    
    """
    # from src.pages.create_project import CreateProjectPage
    # page = CreateProjectPage()
    page = navigate.create_project_page()
    time.sleep(2)
    # Perform project creation
    create_projects([project])
    
    if not project:
        error_fields =  ['name', 'description']
        # Validate error message 'This field is required' appears for all 
        # name and description fields
        for field in error_fields:
            page.validate_p_empty_field_error_msg(field)
    else:
        if name_error:
            # Validate required field error appears only under the Name field
            page.validate_p_name_requird_error_msg()
            page.validate_p_description_requird_error_msg(exists=False)
            
        if descr_error:
            # Validate required field error appears only under the Description field
            page.validate_p_name_requird_error_msg(exists=False)
            page.validate_p_description_requird_error_msg()
            
    # Validate that we stay in createProject page by checking the url
    current_url = CONF.driver.current_url
    assert current_url == "https://pm-tool-e63fa77e3353.herokuapp.com/createProject", "YOU ARE AT WRONG PAGE!"
            
    
def edit_project(project_id, input_data):
    """
        Edit existing projects
        @project_id: Id of the created project
        @param input data: dictionary with the keys (fields) and data (values) to update with
    """
   
    page = navigate.edit_project(project_id)
    time.sleep(2)

    if "name" in input_data.keys():
        page.set_text_input_name(input_data["name"])
        
    if "description" in input_data.keys():
        page.set_text_input_description(input_data["description"])
        
    # Click the Update button
    page.click_button_update()



      