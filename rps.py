import random


def print_rules():
    """Prints the rules of the RPS game."""
    print("Welcome to Rock-Paper-Scissors!")
    print("Choose one: 'rock', 'paper', or 'scissors'.")


def get_player_choice():
    """Asks the player for their choice."""
    choice = input("Enter your choice (rock/paper/scissors): ").lower()
    return choice


def get_computer_choice():
    """Generates a random choice for the computer."""
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    return computer_choice


def determine_winner(player_choice, computer_choice):
    """Determines the winner based on the rules of RPS."""
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
            (player_choice == 'paper' and computer_choice == 'rock') or \
            (player_choice == 'scissors' and computer_choice == 'paper'):
        return "Player wins!"
    else:
        return "Computer wins!"


def play_game():
    """Plays a single round of RPS."""
    print_rules()
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    result = determine_winner(player_choice, computer_choice)
    print(f"Computer chose {computer_choice}.")
    print(result)


def main():
    """Main function to run the game."""
    while True:
        play_game()
        repeat = input("Play again? (y/n): ")
        if repeat.lower() != 'y':
            break


if __name__ == "__main__":
    main()
