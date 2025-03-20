import string
from random import randint


def main():
    password = ""
    print("Password defaults to random, lowercase characters, if you want additional features, answer the questions below.\n")
    pw_length = int(input("How many chars do you want your password to be? "))

    possible_characters = string.ascii_letters + string.punctuation
    for i in range(pw_length):
        random_char = possible_characters[randint(0, len(possible_characters) - 1)]
        password += random_char
    print(password)
    return ""


if __name__ == "__main__":
    main()