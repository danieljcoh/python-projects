import random
import string

"""
TODO
- get phrase
- get number to encrypt by
- show new number
- just make the beginning of it capitalized, ignoring all other grammar
- can only do letters and not symbols
"""

def main():
    letters = string.ascii_lowercase
    encrypt_or_decrypt = input("Encrypt or Decrypt? (e or d)")
    phrase = input("Enter a phrase to encrypt: ").lower()
    number_to_encrypt_by = int(input("Amount: "))
    alphabet = [i for i in letters]
    phrase_list = [i for i in phrase]
    new_phrase = ""

    if encrypt_or_decrypt == "e":
        
        for char in phrase_list:
            char_index = alphabet.index(char)
            char_index += number_to_encrypt_by
            if char_index >= len(letters):
                char_index = char_index % 26
            new_char = alphabet[char_index]
            new_phrase += new_char
        print(new_phrase)

    elif encrypt_or_decrypt == "d":
        for char in phrase_list:
            char_index = alphabet.index(char)
            char_index -= number_to_encrypt_by
            if char_index < 0:
                char_index += 26
            new_char = alphabet[char_index]
            new_phrase += new_char
        print(new_phrase)


if __name__ == "__main__":
    main()
