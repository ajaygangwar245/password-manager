from main import fetch_key, encrypt, decrypt
import sys

def main():
    choice = input("Enter your choice: \n 'show': to see master password \n 'update': to update master password\n> ")

    match choice:
        case 'show':
            show_master()
        case 'update':
            update()
        case _:
            sys.exit("Invalid Choice")

# shows the stored master password
def show_master():
    with open("master.txt", 'r') as file:
        master_password = file.read()

    print(decrypt(master_password))

# updates new password to file
def update():
    new_password = encrypt(input("Please enter new master password: "))

    with open("master.txt", 'w') as file:
        file.write(new_password)


if __name__ == "__main__":
    main()
