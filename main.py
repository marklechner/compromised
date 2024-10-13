def greet_user(name: str) -> str:
    """Greet the user with a simple message."""
    return f"Hello, {name}!"
    
if __name__ == "__main__":
    user_name = input("Enter your name: ")
    print(greet_user(user_name))
