from django.conf import settings

from pycsql.core.manager import Password, String
from pycsql.db.pycsql import pycsql
settings.configure()


def end(command):
    import sys
    if command == "exit":
        sys.exit("Good Bye")


def email():
    _user_email = input("Enter your email: ")
    _user_email_lower = _user_email.lower()
    end(_user_email_lower)
    if _user_email != "":
        return _user_email

    print("You must enter your email first")
    email()


def name():
    user_name = input("\nEnter your full name: ")
    user_name_lower = user_name.lower()
    end(user_name_lower)
    if user_name != "":
        return user_name

    print("You must provide your full name")
    name()


def password():
    user_pass = input("\nEnter Password: ")
    user_pass_lower = user_pass.lower()
<<<<<<< HEAD
    end(user_pass_lower)
    if user_pass != "":
=======
    end(user_pass_lower)            #password is returned in lower case ,, should be rectified later
    if user_pass == "":
        print("You must provide a password")
        password()
    else:
>>>>>>> main
        return user_pass

    print("You must provide a password")
    password()


def conf_password():
    conf_pass = input("\nRetype your password: ")
    conf_pass_lower = conf_pass.lower()
    end(conf_pass_lower)
    if conf_pass != "":
        return conf_pass

    print("You must confirm your password")
    conf_password()


def account():
    print("Please take a minute to create an account")
    get_email = email()
    email_lower = get_email.lower()
    end(email_lower)
    get_name = name()
    name_lower = get_name.lower()
    end(name_lower)
    get_password = password()
    pass_lower = get_password.lower()
    end(pass_lower)
    get_conf_pass = conf_password()
    if get_password != get_conf_pass:
        print("Passwords do not match, please try again")
        account()
    else:
        hashed_pass = Password.hash_password(get_password)
        pycsql.insertData({"email": get_email, "names": get_name, "password": hashed_pass}, "users")
        if pycsql.affectedRows() > 0:
            print("Account Created Successfully")
            another = input("Would you like to create another account? \n [y/n]")
            if another == "y":
                account()
            if another == "n":
                choice = input("Would you like to exit? \n [y/n]")
                if choice == "y":
                    end("exit")
                else:
                    run()
            else:
                _extracted_from_account_31()
        else:
            _extracted_from_account_31()

def _extracted_from_account_31():
    print("Unknown choice")
    print("exiting...")
    end("exit")


def user_email():
    user_em = input("Enter your email: ")
    u_em_lower = user_em.lower()
    end(u_em_lower)
    if user_em != "":
        return user_em

    print("Invalid email address")
    user_email()


def user_password():
    user_pass = input("Enter your password: ")
    u_p_lower = user_pass.lower()
    end(u_p_lower)
    if user_pass != "":
        return user_pass

    print("Password is required")
    user_password()


def login():
    print("LOGIN")
    u_em = user_email()
    u_em_lower = u_em.lower()
    end(u_em_lower)
    u_pass = user_password()
    u_pass_lower = u_pass.lower()
    end(u_pass_lower)
    pycsql.where({"email": u_em})
    data = pycsql.getAll("names, password", 'users')
    __hash = __n = ""
    if len(data) != 0:
        for n, p in data:
            __hash = p
            __n = n
        if Password.password_verify(u_pass, __hash):
            print("Logged in as " + __n)
            account()
        else:
            print("Invalid email or password")
            login()
    else:
        print("Oops, no account matches your login details")
        login()


print("Welcome")


def welcome():
    req = input("\nWhat would you like to do? ")
    import re
    reg = r"[a-zA-Z]"
    if re.match(reg, req):
        return req

    print(req + " is not recognised as a command")
    welcome()


def info():
    u_email = input("Enter your email: ")
    pycsql.where({"email": u_email})
    user_data = pycsql.getAll("names, country, city, contact, dob, img_url", 'users')
    if len(user_data) != 0:

        for names, country, city, contact, dob, img_url in user_data:
            print("\nName: " + names)
            print("Country: " + String.to_string(country))
            print("City: " + String.to_string(city))
            print("Date of birth: " + String.to_string(dob))
            print("Image: " + String.to_string(img_url))
            run()
    else:
        print("No biography associated with the provided email")
        run()


def run():
    request = welcome().lower()
    terminator = request.lower()
    end(terminator)
    if request == "account":
        login()
    elif request == "bio":
        info()
    else:
        print("sorry, I did not understand you")
        run()


def run_cl(r=False):
    if r:
        run()
