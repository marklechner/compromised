from datetime import datetime

def greet_user(name: str) -> str:
    """Greet the user with a time-specific message."""
    current_hour = datetime.now().hour
    if current_hour < 12:
        greeting = "Good morning"
    elif 12 <= current_hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"
        
    return f"{greeting}, {name}!"
