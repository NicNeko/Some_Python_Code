import tkinter as tk
from tkinter import filedialog
from langdetect import detect
from googletrans import Translator
import os


def detect_language(text):
    return detect(text)


def translate_text(text, target_language):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text


def translate_text_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    # Detect the language of the text
    detected_language = detect_language(text)
    print("Detected Language:", detected_language)

    # Translate the text to English
    translated_text = translate_text(text, "en")
    print("Translated Text:")
    print(translated_text)

    # Create a new file with the translated text
    base_path, extension = os.path.splitext(file_path)
    translated_file_path = base_path + "_translated" + extension
    with open(translated_file_path, "w", encoding="utf-8") as translated_file:
        translated_file.write(translated_text)

    print("Translated file created:", translated_file_path)


def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    translate_text_file(file_path)


root = tk.Tk()
root.title("Text Translation")

frame = tk.Frame(root, width=400, height=300)
frame.pack(fill=tk.BOTH, expand=True)

browse_button = tk.Button(frame, text="Browse", command=browse_file)
browse_button.pack(pady=50)

root.mainloop()
