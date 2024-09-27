# PASSWORD MANAGER

#### Video Demo: https://youtu.be/6VL5B-9DPHA

## Description:

This password manager is a command-line application written in Python and designed to securely store and manage user passwords. It supports functionalities such as adding, showing, and deleting passwords, all while ensuring data encryption using a custom key-based cipher. The master password is required for accessing the application, adding an extra layer of security.

### Features:

1. **Master Login**:
   - Before using the application, the user must authenticate with a master password, which is securely encrypted and stored in a file (`master.txt`).

2. **Key-Based Encryption and Decryption**:
   - Passwords are encrypted using a custom cipher, with each character mapped using a predefined key (stored in `key.txt`).
   - The stored passwords are securely encrypted, ensuring that even if unauthorized access occurs, passwords remain unreadable without the correct key.

3. **Password Management**:
   - **Add Password**: Allows users to add a new password for a specified username or email. The password is encrypted before being stored in a CSV file (`passwords.csv`).
   - **Show Password**: Decrypts and displays the password associated with a specified username or email.
   - **Delete Password**: Removes the specified user's password from the CSV file.

4. **Data Storage**:
   - The application stores usernames and their corresponding encrypted passwords in a CSV file (`passwords.csv`).

### Installation:

1. Clone the repository or download the project files.
2. Make sure Python is installed on your system.
3. Ensure the following files are in the project directory:
   - `master.txt`: Contains the encrypted master password.
   - `key.txt`: Contains the cipher key used for encryption/decryption.
   - `passwords.csv`: A CSV file to store username and encrypted password data (if the file doesn't exist, it will be created).

### How to Run:

1. Open a terminal in the project directory.
2. Run the Python script:
```bash
   python password_manager.py
```
3. Enter the master password when prompted. If authenticated, you can choose from the following options:
- `show`: Display the password for a specific user.
- `add`: Add a new username-password pair.
- `delete`: Delete a specific user's password.

### Project Structure:

```bash
password_manager/
│
├── key.txt               # Stores the encryption key
├── master.txt            # Stores the encrypted master password
├── passwords.csv         # Stores usernames and encrypted passwords (created automatically)
└── password_manager.py   # Main Python script
```

### Encryption/Decryption Process:

- The `encrypt` function converts the plain text password into a cipher using a predefined key (loaded from `key.txt`).
- The `decrypt` function reverses the process, converting the encrypted cipher text back into a readable password.

### Dependencies:

- Python 3.x
- `csv` module (pre-installed with Python)

### Future Improvements:
- Support for password complexity generation.
- Implementing password expiration alerts.
- User-friendly GUI interface.
