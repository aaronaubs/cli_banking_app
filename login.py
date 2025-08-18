import users as u
from prompt_toolkit import prompt

def request_login_or_signup():
    """Asks the user to login or signup"""
    print("\nPlease make a selection:")
    print("Login | Signup")
    while True:
        user_input = input("> ").strip().lower()
        valid_inputs = ["login", "log in", "signup", "sign up"]
        if user_input in valid_inputs:
            return user_input
        else:
            print("Please enter 'login' or 'signup'")

def get_username_and_password():
    """
    Gets username and password, then verifies both are correct and correspond to the same account (user_id) before granting access
    """
    username = input("Username: ").strip()    
    password = prompt("Password: ", is_password=True)

    if username in u.usernames:
        user_id = u.usernames[username]
        return username, user_id, password
    else: 
        return "", "", ""

def verify_username_and_password():    
        """Verifies user credentials are correct before logging into account. Handles key error if username not found"""
        while True:
            username, user_id, password = get_username_and_password()
            try:
                if (
                    (username == u.users[user_id]["username"]) and
                    (password == u.users[user_id]["password"])
                    ):
                    print("\nLogin successful!")
                    return
                else:
                    print("Incorrect username or password\n")
                    continue
            
            except KeyError:
                print("Incorrect username or password\n")
                continue

def attempt_login():
    print("\nPlease enter your username and password to login")
    verify_username_and_password()
        
