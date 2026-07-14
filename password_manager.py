import os
import random
import string

FILE_NAME = "passwords.txt"

# ----------------------------

def load_passwords():
    passwords = {}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                data = line.strip().split("|")
                if len(data) == 2:
                    passwords[data[0]] = data[1]
    return passwords

# ----------------------------

def save_passwords(passwords):
    with open(FILE_NAME, "w") as file:
        for account, password in passwords.items():
            file.write(f"{account}|{password}\n")

# ----------------------------

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(random.choice(characters) for _ in range(length))

# ----------------------------

passwords = load_passwords()

while True:

    print("\n==============================")
    print("     PASSWORD MANAGER")
    print("==============================")
    print("1. Add Password")
    print("2. View Password")
    print("3. Show All Accounts")
    print("4. Delete Password")
    print("5. Generate Strong Password")
    print("6. Exit")

    choice = input("\nEnter Choice: ")

    if choice == "1":
        account = input("Account Name: ")
        password = input("Password: ")

        passwords[account] = password
        save_passwords(passwords)

        print("\nPassword Saved Successfully!")

    elif choice == "2":
        account = input("Enter Account Name: ")

        if account in passwords:
            print("\nPassword:", passwords[account])
        else:
            print("\nAccount Not Found!")

    elif choice == "3":
        if passwords:
            print("\nSaved Accounts")
            print("-----------------------")
            for account in passwords:
                print(account)
        else:
            print("\nNo Accounts Saved.")

    elif choice == "4":
        account = input("Enter Account Name to Delete: ")

        if account in passwords:
            del passwords[account]
            save_passwords(passwords)
            print("\nDeleted Successfully!")
        else:
            print("\nAccount Not Found!")

    elif choice == "5":
        length = int(input("Password Length: "))
        new_password = generate_password(length)

        print("\nGenerated Password:")
        print(new_password)

    elif choice == "6":
        print("\nThank You for Using Password Manager!")
        break

    else:
        print("\nInvalid Choice!")