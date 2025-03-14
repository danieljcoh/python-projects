from random import randint


def guessing_game():
    def get_random_number(range):
        random_number = randint(1, range)
        return random_number

    lives = 5
    upper_range_number = int(input("Enter a number: "))
    random_number = get_random_number(upper_range_number)
    print(f"I'm thinking of a number between 1 and {upper_range_number}. Try to guess it. You have {lives} guesses left.")

    past_guesses = list()

    while True:
        guessed_number = int(input("Guess a number: "))
        past_guesses.append(guessed_number)
        if guessed_number == random_number:
            print(f"Congratulations! {guessed_number} is correct! You win! It took you {len(past_guesses)} guesses to guess correctly!")
            break
        else:
            lives -= 1
            if lives == 0:
                print("Game over! I'm sorry. You lose!")
                break
            else:
                print(f"I'm sorry. {guessed_number} is not correct, guess again. You're previous guesses were, {past_guesses}.")
                print(f"You have {lives} guesses left.")

    

# Play the game
guessing_game()