
def change_password():
    "Changes password for admin"
    current_password = input("Enter the current password: ")
    with open("admin_password.txt", "r") as file:
        if current_password != file.read():
            print()
            print("Incorrect password. Access denied.")
            print('***************************************')
            print()
            return

    new_password = input("Enter the new password: ")
    with open("admin_password.txt", "w") as file:
        file.write(new_password)
    print()
    print("Password changed successfully.")
    print('*********************************************')
    print()

def reset_highscore():
    "Reset high score to zero"
    with open("highscore.txt", "w") as file:
        file.write("0,none")
    print("\n****Highscore reset successfully.****\n")

def add_word():
    "adds word to the word.txt file"
    new_word = input("Enter the word to add: ")
    with open("words.txt", "a") as file:
        file.write(" " + new_word)
    print()
    print("Word added successfully.")
    print("*************************************")
    print()

def administrator_interface():
    "Handle and call all the functions of administrator's interface"
    password_correct = True
    while password_correct:
        password_attempt = input("Enter the administrator password: ")
        with open("admin_password.txt", "r") as file:
            password_correct = password_attempt == file.read()
            break
    if not password_correct:
        print()
        print("Incorrect password. Access denied.")
        print()
        administrator_interface()
    print()
    print("Access granted.")
    print('*********************************************')
    print()

    while True:
        print("1. Change password")
        print("2. Reset highscore")
        print("3. Add word")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            change_password()
        elif choice == "2":
            reset_highscore()
        elif choice == "3":
            add_word()
        elif choice == "4":
            break
        else:
            print()
            print("Invalid choice.")
            print('*********************************************')
            print()

