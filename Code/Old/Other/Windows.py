import tkinter as tk
from tkinter import PhotoImage
import os

# Create the main window
window = tk.Tk()

# Set the title of the window
window.title("NekoClient")

# Set the size and position of the window
window.geometry("800x600+100+100")

# Prevent the user from resizing the window
window.resizable(False, False)

# Set the default background color of the window
window.bg = "white"

# Set the icon for the window
window.iconbitmap("C:\\Users\\Nicolas\\Pictures\\NekoClient.ico")

# Load the background image
bg_image = PhotoImage(file="C:\\Users\\Nicolas\\Pictures\\NekoClientBackground.png")

# Create a canvas widget
canvas = tk.Canvas(window, width=800, height=600)

# Create an image on the canvas
canvas.create_image(0, 0, anchor=tk.NW, image=bg_image)

# Place the canvas in the window
canvas.place(x=1, y=1)

# Define the callback functions for the buttons
def on_open_brave_click():
    # Open the Brave browser
    os.startfile("C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe")

def on_open_explorer_click():
    # Open File Explorer
    os.startfile("C:\\Windows\\explorer.exe")

# Create the buttons
open_brave_button = tk.Button(window, text="Open Brave", command=on_open_brave_click,
bg="#7d1710", fg="white", borderwidth=3, highlightthickness=3)
open_explorer_button = tk.Button(window, text="Open Explorer", command=on_open_explorer_click,
bg="#7d1710", fg="white", borderwidth=3, highlightthickness=3)

# Place the buttons in the window
open_brave_button.pack()
open_explorer_button.pack()

# Start the event loop
window.mainloop()
