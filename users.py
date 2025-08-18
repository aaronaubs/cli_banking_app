import re
from prompt_toolkit import prompt

name_pattern = r"[A-Za-z]{1,}"
date_pattern = r"[0-9\/]{10,10}"
username_pattern = r"[A-Za-z0-9\\\/\.\_\-]{5,20}"
password_pattern = r"[A-Za-z0-9!@&\#\.\_\-]{8,25}"

users = {}
usernames = {}

def create_id():
    """Generator function which creates user id values for clients"""
    for i in range(1,100000000):
        yield f"user_{i}"

# Gen variable to grab generator values    
gen = create_id()    

def next_gen():
    """Returns next generator value in sequence"""
    return next(gen)

def set_id():
    """Sets user id value for new user"""
    user_id = next(gen)
    users[user_id] = {}
    return user_id
    
def set_fname(user_id):
    """Creates fname key and sets inputted value into users dictionary"""
    while True:    
        fname = input("Please enter your first name: ").strip()
        if re.match(name_pattern, fname):
            users[user_id]["fname"] = fname
            return fname
        elif len(fname) < 1:
            print("")
        else:
            print("Invalid input. Please try again")

def set_lname(user_id):
    """Creates lname key and sets inputted value into users dictionary"""
    while True:
        lname = input("Please enter your last name: ").strip()
        if re.match(name_pattern, lname):
            users[user_id]["lname"] = lname
            return lname
        elif len(lname) < 1:
            print("")
        else:
            print("Invalid input. Please try again")

def set_birthdate(user_id):
    """Creates birthdate key and sets inputted value into users dictionary"""
    print("Please enter your date of birth (MM/DD/YYYY)")
    while True:
        birthdate = input("> ").strip()
        if re.match(date_pattern, birthdate):
            users[user_id]["birthdate"] = birthdate
            return birthdate
        elif len(birthdate) == 8:
            print("Please include forward slashes")
        else:
            print("Invalid input. Please try again")
                        

def update_fname(user_id):
    """Updates fname value in users dictionary"""
    while True:    
        new_fname = input("\nPlease enter your first name: ").strip()
        if re.match(name_pattern, new_fname):
            users[user_id]["fname"] = new_fname
            return new_fname
        elif len(new_fname) < 1:
            print("")
        else:
            print("Invalid input. Please try again")
    
def update_lname(user_id):
    """Updates lname value in users dictionary"""
    while True:    
        new_lname = input("\nPlease enter your last name: ").strip()
        if re.match(name_pattern, new_lname):
            users[user_id]["lname"] = new_lname
            return new_lname
        elif len(new_lname) < 1:
            print("")
        else:
            print("Invalid input. Please try again")
    
def update_birthdate(user_id):
    """Updates birthdate value in users dictionary"""
    print("\nPlease enter your date of birth (MM/DD/YYYY)")
    while True:
        birthdate = input("> ").strip()
        if re.match(date_pattern, birthdate):
            users[user_id]["birthdate"] = birthdate
            return birthdate
        elif len(birthdate) == 8:
            print("Please include forward slashes")
        else:
            print("Invalid input. Please try again")

def confirm_client_info(user_id):
    """Confirms user's info and allows them to make changes before proceeding"""
    fname = users[user_id]["fname"]
    lname = users[user_id]["lname"]
    birthdate = users[user_id]["birthdate"]
    
    print("\n=====Your Account Info=====\n")
    print(f"First name: {fname}")
    print(f"Last name: {lname}")
    print(f"Date of birth: {birthdate}")

    print("\nIs this info correct? (yes/no)")
    user_input = input("> ").strip().lower()
    if user_input == "yes":
        print("\nExcellent!")
        return
    elif user_input == "no":
        print("\nWhat would you like to change?")
        choices = ["first name", "last name", "date of birth"]
        print("First name | Last name | Date of birth (type 'exit' to go back)")
        choice = input("> ").strip().lower()
        if choice == "exit":
            confirm_client_info(user_id)
        elif choice == "first name":
            update_fname(user_id)
            confirm_client_info(user_id)
        elif choice == "last name":
            update_lname(user_id)
            confirm_client_info(user_id)
        elif choice == "date of birth":
            update_birthdate(user_id)
            confirm_client_info(user_id)
    else:
        print("Invalid input")

def set_username(user_id):
    """Creates username key and sets inputted value into users dictionary""" 
    print("\nPlease enter a username (5-20 characters)")
    print("Valid punctuation: \/._-")
    while True:
        username = input("Username: ").strip()
        if username in usernames:
            print("That username is already taken")
        elif re.match(username_pattern, username):
            users[user_id]["username"] = username
            usernames[username] = user_id
            return username
        elif len(username) < 5 or len(username) > 20:
            print("Please choose a username between 5 and 20 characters long")
        else:
            print("Invalid username")
            print("Only the following punctuation are accepted: \/._-\n")
    
def set_password(user_id):
    """Creates password key and sets inputted value into users dictionary"""
    print("\nPlease enter a password (8-25 characters)")
    print("Valid punctuation: \/._-!@&#")
    while True:
        password = prompt("Password: ", is_password=True)
        if re.match(password_pattern, password):
            password_check = prompt("Confirm password: ", is_password=True)
            if password == password_check:
                users[user_id]["password"] = password
                return password
            else:
                print("Passwords do not match")

        elif len(password) < 8 or len(password) > 25:
            print("Please choose a password between 8 and 25 characters long")
        else:
            print("Invalid password")
            print("Only the following punctuation are accepted: \/._-!@&#\n")


def set_client_info(user_id):
    """Sets account info of new client"""
    print("\nGetting an account set up is fast and easy!")
    print("Please answer a few questions about yourself so we can get you started.\n")
    fname = set_fname(user_id)
    lname = set_lname(user_id)
    birthdate = set_birthdate(user_id)
    confirm_client_info(user_id)
    username = set_username(user_id)
    password = set_password(user_id)