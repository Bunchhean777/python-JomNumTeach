# We're using import a random module to generate a random number.
import random

# Declaring the function for the number guessing game.
def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 5

    print("\n\t>> Welcome to the Number Guessing Game!")
    print("\t>>I have selected a number between 1 and 100.")
    print(f"\n\tYou have {max_attempts} attempts to guess it.\n")

    # If the user has attempts full limite, break the game.
    while attempts < max_attempts:

        # We need to handle invalid inputs using try and exception block.
        try:
            guess = int(input("\tEnter your guess: "))
            attempts += 1

            # Check if the guess is within the valid range of 1 to 100.
            if guess < 1 or guess > 100:
                print("\t❌ Please guess a number between 1 and 100.")
                continue

            # Provide feedback or msg on the guess.
            if guess < number_to_guess:
                print("\t⬆ Too low!")
            elif guess > number_to_guess:
                print("\t⬇ Too high!")
            else:
                print(f"\t🎉 Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
                break
        except ValueError:
            print("\t❌ Invalid input. Please enter a valid number.")

    if attempts == max_attempts:
        print(f"\t❌ Sorry, you've used all your attempts. The number was {number_to_guess}.")

# Calling the function to start the game.
number_guessing_game()