import os
import random
import string
import base64

FILE_NAME = "passwords.txt"
MASTER_PASSWORD = "ritik123"

# Load Passwords
def load_passwords():
    passwords = {}

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                data = line.strip().split("|")

                if len(data) == 2:
                    account = data[0]

                    try:
                        password = base64.b64decode(data[1]).decode()
                    except:
                        password = data[1]

                    passwords[account] = password

    return passwords


# Save Passwords
def save_passwords(passwords):

    with open(FILE_NAME, "w") as file:

        for account, password in passwords.items():

            encoded = base64.b64encode(password.encode()).decode()

            file.write(f"{account}|{encoded}\n")


# Generate Password
def generate_password(length=12):

    chars = string.ascii_letters + string.digits + "!@#$%^&*"

    return "".join(random.choice(chars) for _ in range(length))


# Password Strength
def check_strength(password):

    score = 0

    if len(password) >= 8:
        score += 1

    if any(c.isupper() for c in password):
        score += 1

    if any(c.islower() for c in password):
        score += 1

    if any(c.isdigit() for c in password):
        score += 1

    if any(c in "!@#$%^&*" for c in password):
        score += 1

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"


print("=" * 40)
print("     PASSWORD MANAGER V2")
print("=" * 40)

master = input("Enter Master Password: ")

if master != MASTER_PASSWORD:
    print("Wrong Password!")
    exit()

print("Login Successful!")

passwords = load_passwords()
while True:

    print("\n" + "=" * 40)
    print("       PASSWORD MANAGER V2")
    print("=" * 40)
    print("1. Add Password")
    print("2. View Password")
    print("3. Search Account")
    print("4. Edit Password")
    print("5. Delete Password")
    print("6. Show All Accounts")
    print("7. Generate Strong Password")
    print("8. Exit")

    choice = input("\nEnter Choice: ")

    # ---------------- Add Password ----------------
    if choice == "1":

        account = input("Account Name: ")

        if account in passwords:
            print("\n❌ Account already exists!")
            continue

        password = input("Password: ")

        print("Strength :", check_strength(password))

        passwords[account] = password

        save_passwords(passwords)

        print("\n✅ Saved Successfully!")

    # ---------------- View Password ----------------
    elif choice == "2":

        account = input("Enter Account Name: ")

        if account in passwords:

            print("\nPassword :", passwords[account])

            print("Strength :", check_strength(passwords[account]))

        else:

            print("\n❌ Account Not Found!")

    # ---------------- Search ----------------
    elif choice == "3":

        keyword = input("Search : ").lower()

        found = False

        for account in passwords:

            if keyword in account.lower():

                print("✔", account)

                found = True

        if not found:

            print("\nNo Account Found!")

    # ---------------- Edit ----------------
    elif choice == "4":

        account = input("Enter Account Name: ")

        if account in passwords:

            new_password = input("New Password: ")

            passwords[account] = new_password

            save_passwords(passwords)

            print("\nPassword Updated!")

        else:

            print("\nAccount Not Found!")

    # ---------------- Delete ----------------
    elif choice == "5":

        account = input("Enter Account Name: ")

        if account in passwords:

            confirm = input("Delete? (y/n): ")

            if confirm.lower() == "y":

                del passwords[account]

                save_passwords(passwords)

                print("\nDeleted Successfully!")

            else:

                print("\nCancelled!")

        else:

            print("\nAccount Not Found!")

    # ---------------- Show All ----------------
    elif choice == "6":

        print("\n========== SAVED ACCOUNTS ==========")

        if passwords:

            print("Total Accounts :", len(passwords))

            for account in passwords:

                print("-", account)

        else:

            print("No Accounts Saved!")

    # ---------------- Generator ----------------
    elif choice == "7":

        try:

            length = int(input("Password Length : "))

            new_pass = generate_password(length)

            print("\nGenerated Password :")

            print(new_pass)

            print("Strength :", check_strength(new_pass))

        except:

            print("Invalid Length!")

    # ---------------- Exit ----------------
    elif choice == "8":

        print("\nThank You!")

        break

    else:

        print("\nInvalid Choice!")