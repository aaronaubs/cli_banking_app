import users as u
import login

def greet_client():
    """Shows greeting message to user"""
    print("*" * 40)
    print("Welcome to CLI Bank!")
    

if __name__ == "__main__":
    greet_client()
    user_input = login.check_new_client()
    if user_input == "yes":
        print("\nWelcome back!")
        print("Please enter your username and password to log in")
        username, user_id = login.get_username()
        password = login.get_password(user_id)
        print("Main Menu")

    elif user_input == "no":
        print("")
        user_id = u.set_id()
        u.set_client_info(user_id)
        print("\nYour account is all set up!")
        print("*" * 40)
        print("\nPlease enter your username and password to log in")
        username, _ = login.get_username()
        password = login.get_password(user_id)
        print("Main Menu")