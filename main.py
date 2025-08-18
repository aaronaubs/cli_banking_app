import users as u
import login
import menu

def greet_client():
    """Shows greeting message to user"""
    print("*" * 20)
    print("Welcome to CLI Bank!")
    print("*" * 20)
    

if __name__ == "__main__":
    greet_client()
    user_input = login.request_login_or_signup()
    if user_input == "login" or user_input == "log in":
        login.attempt_login()
        print("Main Menu")

    elif user_input == "signup" or user_input == "sign up":
        user_id = u.set_id()
        u.set_client_info(user_id)
        print("\nYour account is all set up!")
        print("*" * 40)
        login.attempt_login()
        print("Main Menu")