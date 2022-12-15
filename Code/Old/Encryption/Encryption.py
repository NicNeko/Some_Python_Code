# Import the necessary modules
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
import os
import base64

# Open the file that you want to encrypt
file = open("test.txt", "rb")

# Read the contents of the file into memory
file_data = file.read()

# Generate a password for the encryption
password = "my_secret_password"

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

# Encrypt the file data using the Fernet object
encrypted_data = fernet.encrypt(file_data)

# Write the encrypted data to a new file
with open("my_file.encrypted", "wb") as out_file:
    out_file.write(encrypted_data)

# Close the file
file.close()