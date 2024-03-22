import time
ts = str(int(time.time()))


def signup_credentials():
    """
        Returns  dictionaty with valid signup credentials 
    """
    credentials = {
        "fullname": "DummyName" + ts,
        "password": "DummyPassword" + ts,
        "email": f"dummy{ts}@example.com",
        "company": f"DummyCompany{ts}",
        "address": f"DummyAddress{ts}"
    }
    
    return credentials