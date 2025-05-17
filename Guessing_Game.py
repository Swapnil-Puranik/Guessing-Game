#Project: Guessing game for externship
import random # To generate a random number

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100...")
number_to_guess = random.randint(1, 100)

attempts = 0
max_attempts = 10 # allowed attempts is 10

while attempts < max_attempts:
    guess = int(input("Guess the number (between 1 and 100): "))
    attempts += 1

    if guess < number_to_guess: # guessed number is less
        print("Too low! Try again.")
    elif guess > number_to_guess: # guessed number is greater
        print("Too high! Try again.")
    else: # guessed number is correct
        print("Congratulations! You guessed it in ",attempts,"attempts!")
        break
else:
    print("Game over! Better luck next time. The number was", number_to_guess)
