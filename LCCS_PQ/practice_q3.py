# Question 16(a)
# Examination Number: 129478
from random import randint

def guess_game():
    print("Welcome to the guessing game!")
    difficulty = input("Enter difficulty (E)asy or (H)ard: ").lower()
    max_guesses_allowed = int(input("Enter the maximum number of guesses allowed: "))
    
    secret_number = randint(1, 100 if difficulty == "h" else 5)
    guessed_numbers = set()  # Use a set to store guessed numbers for faster lookup
    guess_count = 0
    
    while guess_count < max_guesses_allowed:
        try:
            user_guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        
        if user_guess in guessed_numbers:
            print("You already guessed this number.")
            continue
        
        guessed_numbers.add(user_guess)
        guess_count += 1
        
        if user_guess == secret_number:
            print(f"Congratulations! You win! You took {guess_count} guesses.")
            return
        
        print("Too low" if user_guess < secret_number else "Too high")
    
    print(f"Too many guesses. The secret number was {secret_number}.")

guess_game()
