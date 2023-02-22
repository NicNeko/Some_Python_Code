# import the gTTS library and the os library
from gtts import gTTS
import os

# ask the user for input
text = input("Enter the text you want to convert to speech: ")

# create a gTTS object
tts = gTTS(text=text, lang='en')

# create a filename based on the user input
filename = f"{text[:10]}.mp3"  # take the first 10 characters of the input and use as filename

# save the audio file with the filename
tts.save(filename)

# play the audio file using Windows Media Player
os.startfile(filename)
