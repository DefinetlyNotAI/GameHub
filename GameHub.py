import tkinter as tk

root = tk.Tk()
root.title("Game Selector")


# Define the game functions
def mastermind():
    print("Mastermind")


def rock_paper_scissors():
    print("Rock Paper Scissors")


def hangman():
    print("Hangman")


def tic_tac_toe():
    print("Tic Tac Toe")


# Map game names to their corresponding functions
games = {
    "Rock Paper Scissors": rock_paper_scissors,
    "Hangman": hangman,
    "Tic Tac Toe": tic_tac_toe,
    "Mastermind": mastermind
}

for _, (game_name, game_func) in enumerate(games.items()):
    # Create a button for each game
    btn = tk.Button(root, text=game_name, command=lambda i=_, game_func=games[game_name]: game_func())
    btn.pack(pady=10)

# Start the main loop
root.mainloop()
