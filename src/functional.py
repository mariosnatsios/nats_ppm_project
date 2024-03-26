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
    # Check invalid email format error message       
    if invalid_email:
        signup_page.validate_p_invalid_email_error_msg()
    # Check already existing email error message
    if existing_email:
        signup_page.validate_p_already_exist_email_error_msg(email=data["email"])
        
     # Validate current url
    current_url = CONF.driver.current_url
    assert current_url == "https://pm-tool-e63fa77e3353.herokuapp.com/signup", "NOT THE CORRECT LANDING PAGE!!"
        
        
    
    