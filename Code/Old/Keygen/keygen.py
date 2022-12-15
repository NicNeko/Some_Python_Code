import random
from datetime import datetime

# Set the length of the key
KEY_LENGTH = 69

# Prompt the user for input
prompt = "Enter the Username for the key: "
name = input(prompt)

# Open a file for writing the key
with open('keys.txt', 'a') as f:
    # Generate a random key
    key = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(KEY_LENGTH))

    # Get the current date and time
    now = datetime.now()

    # Format the date and time as a string
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

    # Write the key and date/time to the file
    f.write(name + ': ' + key + ' ' + date_time + '\n')

    # Print the key and date/time
    print(name + ': ' + key + ' ' + date_time)
