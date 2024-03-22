from src.urls import Navigate
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
        
    # Clicks the Sighn Up button
    page.click_button_sign_up()
    
    