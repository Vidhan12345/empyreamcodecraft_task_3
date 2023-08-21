import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# Set the initial number of attempts
attempts = 0

while True:
    # Ask the user to guess the number
    guess = int(input("Take a guess: "))

    # Increase the number of attempts
    attempts += 1

    if guess < secret_number:
        print("Your number is too low! Try again.")
    elif guess > secret_number:
        print("Your number is too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
        break
