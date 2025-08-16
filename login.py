import users as u
from prompt_toolkit import prompt

def get_username():
    """
    Gets user username input and verifies username exists in database, then returns username and user_id values
    """
    while True:
        username = input("Username: ").strip()
        if username in u.usernames:
            break
        else:
            print("That username does not exist")
    
    user_id = u.usernames[username]
    return username, user_id

def get_password(user_id):
    """
    Gets user password input confidentially and verifies password corresponds to account username
    """
    while True:
        password = prompt("Password: ", is_password=True)
        if password == u.users[user_id]["password"]:
            break
        else:
            print("Incorrect password")
    
    print("\nLogin successful!")
