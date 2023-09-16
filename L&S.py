# Imports
import time
import sys
import random
import string

# Information
developer = "GeneralAce"
version = "Beta 1.1.2"

# Variables
boot_type = 3

s_username = None
s_password = None

l_username = None
l_password = None

logged_in = False

PG_chosen = False


# Clear screen code
def cs():
    clear_screen_var = 0
    while clear_screen_var < 100:
        print("")
        clear_screen_var += 1
    if clear_screen_var >= 100:
        clear_screen_var = 0



# Bootloader
def boot_loader():
    
    # Login function
    def login_boot():
        
        global logged_in
        global l_username
        global l_password
        
        print("Booted into login mode.")
        time.sleep(1)
        cs()

        # Login system
        while True:
            l_username = input("Enter your username >> ")
            
            # Opens the username file
            with open(l_username + ".txt", "r") as username_login_verifier:
                verify_user = username_login_verifier.read()

            # Verifies the username
            if verify_user == l_username:
                print("Verified username.")
                time.sleep(1)
                cs()

                l_password = input("Enter your password >> ")

                # Opens the password file
                with open(l_username + "_password.txt", "r") as password_login_verifier:
                    verify_password = password_login_verifier.read()

                # Verifies the password
                if verify_password == l_password:
                    print("Verified password.")
                    time.sleep(1)
                    cs()
                logged_in = True
            break




    # Signup function
    def signup_boot():
        
        global logged_in
        global s_username
        global s_password

        print("Booted into signup mode.")
        time.sleep(1)
        cs()

        # Signup system
        while True:
            s_username = input("Enter your desired username >> ")
            s_username_req = len(s_username)
            if s_username_req < 2:
                print("ERROR! Your username must be at least 2 characters long.")
                time.sleep(1)
                cs()
            else:
                cs()
                while True:
                    s_password = input("Enter your desired password >> ")
                    s_password_req = len(s_password)
                    if s_password_req < 8:
                        print("ERROR! Your password must be at least 8 characters long.")
                        time.sleep(1)
                        cs()
                    else:
                        print("Creating account.")
                        time.sleep(1)
                        print("Creating account..")
                        time.sleep(1)
                        print("Creating account...")

                        # Account information saver
                        with open(s_username + ".txt", "w") as user_writer:
                            user_writer.write(s_username)
                        with open(s_username + "_password.txt", "w") as password_writer:
                            password_writer.write(s_password)
                        cs()
                        print("Successfully signed up!")
                        time.sleep(1)
                        cs()
                        logged_in = True
                        break
                    break
                break



    if boot_type == 0:
        login_boot()
    elif boot_type == 1:
        signup_boot()
    else:
        print("ERROR! Unknown boot error!")
        time.sleep(1)
        print("Please restart the application.")
        time.sleep(2)
        cs()
        print("Automatically closing the app in 3s.")
        time.sleep(1)
        print("Automatically closing the app in 2s..")
        time.sleep(1)
        print("Automatically closing the app in 1s...")
        time.sleep(1)
        sys.exit(1)




# Startup code
def startup():
    
    def starting_up_loader():
        print("Starting up.")
        time.sleep(1)
        print("Starting up..")
        time.sleep(1)
        print("Starting up...")
        time.sleep(1)
        print("Starting up.")
        time.sleep(1)
        print("Starting up..")
        time.sleep(1)
        print("Starting up...")
        time.sleep(1)
        cs()
    starting_up_loader()

    # Boots into the right mode(login/signup)
    def startup_type():
        
        global boot_type
        
        while True:
            startup_type_identifier = input("Boot into login or sign up(L/S) >> ")
            if startup_type_identifier == "L":
                print("Booting into login.")
                time.sleep(1)
                print("Booting into login..")
                time.sleep(1)
                cs()

                boot_type = 0
                break
            elif startup_type_identifier == "S":
                print("Booting into signup.")
                time.sleep(1)
                print("Booting into signup..")
                time.sleep(1)
                cs()

                boot_type = 1
                break
            else:
                print("ERROR! Please type only \"L\" or \"S\".")
                cs()
    startup_type()

    boot_loader()

startup()

# Makes the user choose to open an application
def choose_app():

    global PG_chosen

    ca = input("Choose an application: Password generator(write: \"PG\")")
    if ca == "PG":
        cs()
        print("Loading password generator.")
        time.sleep(1)
        print("Loading password generator..")
        time.sleep(1)
        print("Loading password generator...")
        PG_chosen = True
        cs()

def password_generator():
    pass

def app_loader():

    global PG_chosen

    if PG_chosen == True:
        password_generator()
    else:
        pass