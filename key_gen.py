import random
import string
import sys

def main():
    choice = input("Enter your choice: \n 'show': to view stored key \n 'gen': to generate new key\n> ")

    match choice:
        case 'show':
            show_key()
        case 'gen':
            generate()
        case _:
            sys.exit("Invalid Choice")

# shows the stored key
def show_key():
    with open("key_gen.txt", 'r') as file:
        key = file.read()

    print(key)

# generates new key and add it to file
def generate():
    chars = string.punctuation + string.ascii_letters + string.digits
    chars = list(chars)
    temp  = chars.copy()

    # random list of characters
    random.shuffle(temp)

    # create key string
    key = ""
    for i in range(len(temp)):
        key += temp[i]

    with open("key_gen.txt", 'w') as file:
        file.write(key)


if __name__ == "__main__":
    main()