def translate(message, to_morse=True):
    # Morse code dictionary
    morse_code = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
                  'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
                  'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
                  'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                  'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
                  'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
                  '4': '....-', '5': '.....', '6': '-....', '7': '--...',
                  '8': '---..', '9': '----.', '0': '-----', ' ': '/'}

    if to_morse:
        # Translate the message to Morse code
        translated_message = ''
        for char in message:
            char = char.upper()
            if char in morse_code:
                translated_message += morse_code[char] + ' '
            else:
                translated_message += char

        return translated_message
    else:
        # Translate the message from Morse code
        translated_message = ''
        message = message.split(' ')
        for char in message:
            for key, value in morse_code.items():
                if char == value:
                    translated_message += key

        return translated_message


def main():
    while True:
        choice = input("Do you want to translate to Morse code (1) or from Morse code (2)? ")

        if choice == '1':
            message = input("Enter the message to translate: ")
            translated_message = translate(message)
            print("Translated message:", translated_message)
        elif choice == '2':
            message = input("Enter the Morse code to translate: ")
            translated_message = translate(message, to_morse=False)
            print("Translated message:", translated_message)
        else:
            print("Invalid choice.")
            continue

        repeat = input("Do you want to translate another message (yes/no)? ")
        if repeat.lower() == 'no':
            break


if __name__ == '__main__':
    main()
