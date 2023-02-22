import os

# Ask for customer name and create folder
customer_name = input("Enter customer name: ")
customer_folder = os.path.join(os.path.expanduser("~"), "Desktop", customer_name)
if not os.path.exists(customer_folder):
    os.mkdir(customer_folder)

# Create avatar folder
avatar_folder = os.path.join(customer_folder, "Avatar")
if not os.path.exists(avatar_folder):
    os.mkdir(avatar_folder)

# Ask for avatar name and create subfolder
avatar_name = input("Enter avatar name: ")
avatar_subfolder = os.path.join(avatar_folder, avatar_name)
if not os.path.exists(avatar_subfolder):
    os.mkdir(avatar_subfolder)

print(f"Folder structure created for {customer_name} with avatar {avatar_name}.")
