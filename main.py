import csv
import sys


# fetches key from the text file
def fetch_key():
    with open('key.txt', 'r') as file:
        key = file.read()
    return list(key)

# global variable
key = fetch_key()


# MAIN FUNCTION
def main():
    # attempts login into password manager
    attempts = 3
    while attempts >= 1:
        pwd = input("Enter master password to open password manager: ")
        if login(pwd):
            print("Login successfull! :)")
            break
        elif attempts == 1:
            sys.exit("Login Failed! :(")
        else:
            attempts -= 1
            continue

    # ask user for tasks to perform in password manager
    while True:
        task = input("Enter your choice: \n > 'show' : to show password \n > 'add' : to add new password \n > 'delete' : to delete a password\n")

        # asking for username
        username = input("Enter account's username or e-mail: ")

        # matches user's choice to perform appropriate task
        match task:
            case 'show':
                val= show(username)
                print(f"{val}")
                break
            case 'add':
                password = input("Enter password to be secured: ")
                val= add(username, password)
                print(f"{val}")
                break
            case 'delete':
                val= delete(username)
                print(f"{val}")
                break
            case _:
                print("Invalid choice! please try again")


# to login into password manager
def login(password):
    # reads master password from text file
    with open('master.txt', 'r') as file:
        master_password = file.read()

    # decrpyts master password
    master_password = decrypt(master_password)

    # matches user input with master password
    if password == master_password:
        return True
    return False


# encrypts the password using key
def encrypt(plain_password):

    # global keyword for key
    global key
    cipher_password = ""

    # encrypts plain password using key and using reference from ascii codes
    for letter in plain_password:
        index = ord(letter) - 33
        cipher_password += key[index]

    return cipher_password


# decrypts the password using key
def decrypt(cipher_password):

    # global keyword for key
    global key
    plain_password = ""

    # decrypt cipher password using key
    for letter in cipher_password:
        index = key.index(letter) + 33
        plain_password += chr(index)

    return plain_password


# show password using username
def show(username):
    password = ""

    # reading password from file
    with open('passwords.csv', 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if username == row["username"]:
                password = row["password"]
                break
        else:
            return "User doesn't exists!"

    # decrypting password
    return decrypt(password)


# add new password to file
def add(username, password):
    # encrypting password
    cipher_password = encrypt(password)

    # adding to the passwords file
    with open('passwords.csv', 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["username", "password"])
        writer.writerow({"username": username, "password": cipher_password})

    return "Added successfully"


# delete password from the file
def delete(username):
    passwords = []

    # flag to track if user is found
    user_found = False

    # read passwords data from file
    with open('passwords.csv', 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if username == row["username"]:
                user_found = True
            else:
                passwords.append({"username": row["username"], "password": row["password"]})

    # if user not found
    if not user_found:
        return "User doesn't exists!"

    # writes header to passwords file
    with open('passwords.csv', 'w', newline='') as writefile:
        writer = csv.DictWriter(writefile, fieldnames=["username", "password"])
        writer.writerow({"username": "username", "password": "password"})

    # writes new data to passwords file
    with open('passwords.csv', 'a', newline='') as writefile:
        writer = csv.DictWriter(writefile, fieldnames=["username", "password"])
        for row in passwords:
            writer.writerow({"username": row["username"], "password": row["password"]})

    return "User deleted successfully"


if __name__ == "__main__":
    main()
