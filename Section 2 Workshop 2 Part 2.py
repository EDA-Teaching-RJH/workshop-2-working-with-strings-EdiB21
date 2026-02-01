import random


secret_number = random.randint(1, 10)

user_guess = int(input("Guess a number between 1 and 10: "))

if user_guess == secret_number:
    print("You guessed the correct number!")
elif user_guess > secret_number:
    print("Too high!, Try again.")
elif user_guess < secret_number:
    print("Too low!, Try again.")

