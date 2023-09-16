# Imports
import ast
import time
import sys

# Information
developer = "GeneralAce"
version = "Alpha 1.0.0"

# Variables
boot_type = 3

# Clear screen code
def cs():
    clear_screen_var = 0
    while clear_screen_var < 100:
        print("")
        clear_screen_var += 1
    if clear_screen_var >= 100:
        clear_screen_var = 0


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

    def startup_type():
        while True:
            startup_type_identifier = input("Boot into login or sign up(l/s) >> ")
            if startup_type_identifier == "l":
                print("Booting into login.")
                time.sleep(1)
                print("Booting into login..")
                time.sleep(1)
                cs()

                boot_type = 0
                break
            elif startup_type_identifier == "s":
                print("Booting into signup.")
                time.sleep(1)
                print("Booting into signup..")
                time.sleep(1)
                cs()

                boot_type = 1
                break
            else:
                print("Please type only \"l\" or \"s\".")
                cs()
    startup_type()

def boot_loader():
    
    def login_boot():
        pass

    def signup_boot():
        pass

    if boot_type == 0:
        login_boot()
    elif boot_type == 1:
        signup_boot()
    else:
        print("Unknown boot error!")
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

startup()