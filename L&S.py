# Imports
import time
import sys
import random
import string
import math

# Information
developer = "GeneralAce"
version = "Beta 1.5.5"

# Variables
boot_type = 3

s_username = None
s_password = None

l_username = None
l_password = None

logged_in = False

PG_chosen = False
password_length = 12

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
        while logged_in == False:
            l_username = input("Enter your username >> ")
            
            # Opens the username file
            with open(l_username + ".txt", "r") as username_login_verifier:
                verify_user = username_login_verifier.read()

                # Verifies the username
            while logged_in == False:    
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
                    else:
                        print("ERROR! Enter a valid password.")
                        time.sleep(1)
                        cs()
                else:
                    print("ERROR! Enter a valid username.")
                    time.sleep(1)
                    cs()
                




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

    ca = input("Choose an application: Password generator(write: \"PG\") >> ")
    if ca == "PG":
        cs()
        print("Loading password generator.")
        time.sleep(1)
        print("Loading password generator..")
        time.sleep(1)
        print("Loading password generator...")
        PG_chosen = True
        cs()

        app_loader()


# Password generator system
def password_generator(password_length):
    
    # Password generator code
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(password_length))

    return password

def calculator():
    
    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        if y == 0:
            return "ERROR! Division by zero"
        return x / y

    def exponentiate(x, y):
        return x ** y

    def take_root(x, y):
        if x < 0 and y % 2 == 0:
            return "ERROR! Cannot take even root of a negative number"
        return x ** (1 / y)

    def calculator_ui():

        while True:
            
            print("Simple Calculator")
            print("Available operations:")
            print("1. Addition (+)")
            print("2. Subtraction (-)")
            print("3. Multiplication (*)")
            print("4. Division (/)")
            print("5. Exponentiation (^)")
            print("6. Root (√)")
            print("Enter 'q' to quit")
            print("")
            
            choice = input("Select operation (1/2/3/4/5/6/q): ")

            if choice == 'q':
                print("Closing calculator.")
                time.sleep(1)
                sys.exit()
            elif choice in ('1', '2', '3', '4', '5', '6'):
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    print("Result: ", add(num1, num2))
                elif choice == '2':
                    print("Result: ", subtract(num1, num2))
                elif choice == '3':
                    print("Result: ", multiply(num1, num2))
                elif choice == '4':
                    print("Result: ", divide(num1, num2))
                elif choice == '5':
                    print("Result: ", exponentiate(num1, num2))
                elif choice == '6':
                    print("Result: ", take_root(num1, num2))
            else:
                print("Invalid input. Please try again.")
            
            while True:
                again_C = input("Do you want to make a new calculation?(y/n) >> ")    
                if again_C == "y":
                    break
                elif again_C == "n":
                    sys.exit()
                else:
                    print("ERROR! Please type \"y\" or \"n\".")

# Password generator input & output system
def pg_i_and_o_s():
    
    global again_PG_var
    global password_length

    while True:
        while True:
            try:
                password_length = int(input("How long do you want your password to be? (8-128 characters) >> "))
                
                # Makes sure that the input is an integer between 8 and 128
                if 8 <= password_length <= 128:
                    break
                else:
                    print("Please enter a valid number between 8 and 128.")
            except ValueError:
                print("Please enter a valid integer.")

        cs()
        generated_password = password_generator(password_length)

        print("Your generated password is:", generated_password)
        time.sleep(1)

        while True:
            again_PG = input("Do you want to create a new password?(y/n) >> ")    
            if again_PG == "y":
                break
            elif again_PG == "n":
                sys.exit()
            else:
                print("ERROR! Please type \"y\" or \"n\".")



# App loader system
def app_loader():

    global PG_chosen

    if PG_chosen == True:
        cs()
        pg_i_and_o_s()
    else:
        pass

choose_app()