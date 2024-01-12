import playersfile
def selecting():
    """Check if user is an already existing or a new one."""
    print("LOGIN to coninue or SIGNUP")
    choice = input("Enter an option, Login or Signup (L\S): ").upper()
    if choice == "L":
        login()
    elif choice == "S":
        signup()
    else:
        print("Enter a valid choice")
        selecting()
def listing_database():
    '''serches for user's record in database'''
    with open("Database.txt", "r+") as db:
        login_details = (db.readlines())
    return login_details
def signup():
    '''This function is used to direct user to signup if player did not have account. '''

    print('''Instructions:
    1- The username should be valid and not pre-existing.
    2- Password should not be less than 6 characters.''')

    username = input("Enter a Username: ").lower()
    password = input("Enter a Password: ")
    password1 = input("Confirm your password: ")

    with open("Database.txt", "r") as db:
        checking_username = db.readlines()
        count = 0
        for i in checking_username:
            if username in i:
                count += 1
        if count != 0:
            print("Username already exist!")
            signup()
        else:
            if password != password1:
                print("Check and confirm password again!")
                signup()
            elif len(password)<6:
                print("Password is too short!")
                signup()
            else:
                with open("Database.txt", "a") as db:
                    db.write("\n")
                    db.write(username + "," + password)
                    print("Account created!")
                    playersfile.play_hangman()

def login():
    '''Validates id of an existing user to grant access in to the game'''
    print("LOGIN ACCOUNT")
    login_details = listing_database()
    username = input("Enter your user name: ").lower()
    password = input("(password is case sensitive)\nEnter your password: ")
    l = 0
    for i in login_details:
        if username in i and password in i:
            print("Successfully logged in!")
            l+=1
            playersfile.play_hangman()
    if l < 1:
        print("\nLogin failed!!\nPlease try again.")
        print()
        login()






