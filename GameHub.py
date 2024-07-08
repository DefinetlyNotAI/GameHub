from Hangman import Hangman_game as hg
from Mastermind import play_mastermind as mm
from RPS import rps
from TicTacToe import ttt, tk

root = tk.Tk()
root.title("Game Selector")

# Map game names to their corresponding functions
games = {
    "Rock Paper Scissors": rps,
    "Hangman": hg,
    "Tic Tac Toe": ttt,
    "Mastermind": mm,
}

for _, (game_name, game_func) in enumerate(games.items()):
    # Create a button for each game
    btn = tk.Button(
        root,
        text=game_name,
        command=lambda i=_, game_func=games[game_name]: game_func(),
    )
    btn.pack(pady=10)

# Start the main loop
root.mainloop()
