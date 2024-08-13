
translate_dict =  {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
    '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', ' ': '/'
    }
is_on = True

while is_on:
    option = input("Enter an option, Encode or Decode\n").lower()
    if option == "encode":
        # Create a function called text_to_morse_code and pass in text as input.
        def text_to_morse_code(text):
            morse_code = ""
            # Get hold of each character of the input text from the user and convert it to morse code.
            for x in text:
                # Add space inbetween characters in the morse_code variable.
                morse_code += translate_dict[x.upper()] + ' '
            return morse_code
        text = input("Enter text to convert to morse code")
        # Print out the morse code passing the text from the user as the input.
        print(text_to_morse_code(text))

    elif option == "decode":
        # Get the reverse of the translate_dict (morse dictionary)
        reverse_translate_dict = {v: k for k, v in translate_dict.items()}


        # Create a function called morse_code_to_tex and pass in morse_codes as input.
        def morse_code_to_text(morse_codes):
            reverse_text = ""
            # Get the characters representing each letter in a text
            for k in morse_codes.split(" "):
                if k == '':
                    pass
                else:
                    reverse_text += reverse_translate_dict[k]
            return reverse_text
        morse_codes = input("Enter morse code to convet to text.")
        # Print out the text passing the morse_code from the user as the input.
        print(morse_code_to_text(morse_codes))

    else:
        print("Invalid input, try again")




