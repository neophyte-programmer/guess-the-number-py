import random


def guessNumber(x):
    random_number = random.randint(1, x)
    guess = 0

    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))

        if guess < random_number:
            print("Oops! Guess a higher number.")
        elif guess > random_number:
            print("Oops! Guess a lower number.")

    print("Yay, you guessed the right number!")


guessNumber(10)
