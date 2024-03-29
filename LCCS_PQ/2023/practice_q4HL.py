import random

def get_score(secret_number, guess):
    difference = abs(secret_number - guess)
    if difference == 0:
        return 100, "JACKPOT!!! You score 100 points"
    elif difference <= 20:
        return 20, "You score 20 points"
    elif difference > 30:
        return -30, "You lose 30 points"
    else:
        return 0, ""

def play_game():
    score = 0
    play_again = True

    while play_again:
        secret_number = random.randint(1, 100)
        guess = 0

        while guess not in range(1, 101):
            try:
                guess = int(input("Enter your guess (1-100): "))
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 100.")

        difference = abs(secret_number - guess)
        print(f"Secret number is {secret_number}. You guessed {guess}. Difference is {difference}.")

        points, message = get_score(secret_number, guess)
        score += points
        print(message)
        print(f"Your current score is {score}")

        while True:
            play_again_input = input("Play again? (Y/N): ").upper()
            if play_again_input == 'Y':
                break
            elif play_again_input == 'N':
                play_again = False
                break
            else:
                print("Invalid input. Please enter 'Y' or 'N'.")

    print("Thanks for playing!")

if __name__ == '__main__':
    play_game()