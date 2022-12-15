import random
import sqlite3
from datetime import datetime

# Set the length of the key
KEY_LENGTH = 69

# Prompt the user for input
prompt = "Enter a name for the key: "
name = input(prompt)

# Generate a random key
key = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(KEY_LENGTH))

# Get the current date and time
now = datetime.now()

# Format the date and time as a string
date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

# Connect to the database
connection = sqlite3.connect("keys.db")

# Create a cursor
cursor = connection.cursor()

# Execute an SQL query to insert the key, name, and date/time into the database
cursor.execute("INSERT INTO keys (name, key, date_time) VALUES (?, ?, ?)", (name, key, date_time))

# Commit the transaction
connection.commit()

# Close the connection
connection.close()

# Print the key and date/time
print(name + ': ' + key + ' ' + date_time)
