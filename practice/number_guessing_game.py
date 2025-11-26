# We're using import a random module to generate a random number.
import random

# declaring varibales
number_to_guess = random.randint(1, 100)
attempts = 0
max_attempts = 10

print("\n> Welcome to the Number Guessing Game!")
print("> You have selected a number between 1 and 100.")
print(f"\nYou have {max_attempts} attempts to guess it.\n")   
    
# If the user has attempts full limite, break the game.
while attempts < max_attempts:

    # We need to handle invalid inputs using try and exception block.
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        # Check if the guess is within the valid range of 1 to 100.
        if guess < 1 or guess > 100:
            print("\n❌ Please guess a number between 1 and 100.")
            continue

        # Provide feedback or msg on the guess.
        if guess < number_to_guess:
            print("⬆ Too low!")
        elif guess > number_to_guess:
            print("⬇ Too high!")
        else:
            print(f"\n🎉 Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
            break
    except ValueError:
        print("\n❌ Invalid input. Please enter a valid number.")

    # If the user has used all attempts, reveal the number.
    if attempts == max_attempts:
        print(f"\n❌ Sorry, you've used all your attempts. The number was {number_to_guess}.")