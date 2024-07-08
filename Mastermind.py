import random


def generate_secret_code():
    """Generates a random secret code."""
    return [random.randint(0, 9) for _ in range(4)]


def get_player_guess():
    """Gets the player's guess as a list of integers."""
    while True:
        try:
            guess = list(map(int, input("Enter your 4-digit guess: ").strip()))
            if len(guess) == 4 and all(0 <= num < 10 for num in guess):
                return guess
            else:
                print("Invalid guess. Please enter a 4-digit number.")
        except ValueError:
            print("Invalid input. Please enter a 4-digit number.")


def provide_feedback(secret_code, guess):
    """Provides feedback on the player's guess."""
    correct_in_position = sum(a == b for a, b in zip(secret_code, guess))
    correct_not_in_position = sum(
        min(secret_code.count(c), guess.count(c)) for c in set(secret_code + guess)
    )
    return correct_in_position, correct_not_in_position - correct_in_position


def play_mastermind():
    secret_code = generate_secret_code()
    amount = 0
    while True:
        guess = get_player_guess()
        correct, incorrect = provide_feedback(secret_code, guess)
        print(f"Correct in position: {correct}")
        print(f"Incorrect but present: {incorrect}")
        amount += 1
        if guess == secret_code:
            print("Congratulations! You've guessed the code.")
            print(f"It took you {amount} guesses.")
            break


if __name__ == "__main__":
    play_mastermind()
