"""A tic-tac-toe game built with Python and Tkinter."""

import tkinter as tk
from itertools import cycle
from tkinter import font
from typing import NamedTuple


class Player(NamedTuple):
    label: str
    color: str


class Move(NamedTuple):
    row: int
    col: int
    label: str = ""


BOARD_SIZE = 3
DEFAULT_PLAYERS = (
    Player(label="X", color="blue"),
    Player(label="O", color="green"),
)


class TicTacToeGame:
    def __init__(self, players=DEFAULT_PLAYERS, board_size=BOARD_SIZE):
        """
        Initialize the TicTacToeGame with the specified players and board size.

        Parameters:
            players (tuple): A tuple of Player objects representing the players of the game.
            board_size (int): The size of the game board.

        Returns:
            None
        """
        self._players = cycle(players)
        self.board_size = board_size
        self.current_player = next(self._players)
        self.winner_combo = []
        self._current_moves = []
        self._has_winner = False
        self._winning_combos = []
        self._setup_board()

    def _setup_board(self):
        """
        Initializes the game board by creating a 2D list of Move objects representing the current moves
        and a list of winning combinations.

        This function creates a 2D list of Move objects, where each Move object represents a cell on the
        game board. The Move object has three attributes: row, col, and label. The row and col attributes
        represent the position of the cell on the board, and the label attribute represents the label
        of the player who made the move.

        The function also calls the _get_winning_combos() method to get a list of winning combinations.
        These combinations are used to check if a player has won the game.

        Parameters:
            self (TicTacToeGame): The TicTacToeGame object.

        Returns:
            None
        """
        self._current_moves = [
            [Move(row, col) for col in range(self.board_size)]
            for row in range(self.board_size)
        ]
        self._winning_combos = self._get_winning_combos()

    def _get_winning_combos(self):
        """
        Generate a list of winning combinations for the Tic-Tac-Toe game.

        This function creates winning combinations by combining rows, columns, and diagonals of the current game board.
        The winning combinations are used to determine if a player has won the game.

        Parameters:
            self (TicTacToeGame): The TicTacToeGame object.

        Returns:
            list: A list of winning combinations.
        """
        rows = [[(move.row, move.col) for move in row] for row in self._current_moves]
        columns = [list(col) for col in zip(*rows)]
        first_diagonal = [row[i] for i, row in enumerate(rows)]
        second_diagonal = [col[j] for j, col in enumerate(reversed(columns))]
        return rows + columns + [first_diagonal, second_diagonal]

    def is_valid_move(self, move):
        """Return True if move is valid, and False otherwise."""
        row, col = move.row, move.col
        move_was_not_played = self._current_moves[row][col].label == ""
        no_winner = not self._has_winner
        return no_winner and move_was_not_played

    def process_move(self, move):
        """Process the current move and check if it's a win."""
        row, col = move.row, move.col
        self._current_moves[row][col] = move
        for combo in self._winning_combos:
            results = set(self._current_moves[n][m].label for n, m in combo)
            is_win = (len(results) == 1) and ("" not in results)
            if is_win:
                self._has_winner = True
                self.winner_combo = combo
                break

    def has_winner(self):
        """Return True if the game has a winner, and False otherwise."""
        return self._has_winner

    def is_tied(self):
        """Return True if the game is tied, and False otherwise."""
        no_winner = not self._has_winner
        played_moves = (move.label for row in self._current_moves for move in row)
        return no_winner and all(played_moves)

    def toggle_player(self):
        """Return a toggled player."""
        self.current_player = next(self._players)

    def reset_game(self):
        """Reset the game state to play again."""
        for row, row_content in enumerate(self._current_moves):
            for col, _ in enumerate(row_content):
                row_content[col] = Move(row, col)
        self._has_winner = False
        self.winner_combo = []


class TicTacToeBoard(tk.Tk):
    def __init__(self, game):
        """
        Initialize the TicTacToeBoard with the specified game object.

        Parameters:
            game: The game object associated with the board.

        Returns:
            None
        """
        super().__init__()
        self.title("Tic-Tac-Toe Game")
        self._cells = {}
        self._game = game
        self._create_menu()
        self._create_board_display()
        self._create_board_grid()

    def _create_menu(self):
        """
        Create the menu bar for the Tic-Tac-Toe game window.
        """
        menu_bar = tk.Menu(master=self)
        self.config(menu=menu_bar)
        file_menu = tk.Menu(master=menu_bar)
        file_menu.add_command(label="Play Again", command=self.reset_board)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

    def _create_board_display(self):
        """
        Creates a frame and a label to display the game board.

        This function creates a new frame and sets it as the master for the label.
        The label is then configured with the text "Ready?" and a font size of 28.
        The label is packed into the frame.

        Parameters:
            self (TicTacToeBoard): The instance of the TicTacToeBoard class.

        Returns:
            None
        """
        display_frame = tk.Frame(master=self)
        display_frame.pack(fill=tk.X)
        self.display = tk.Label(
            master=display_frame,
            text="Ready?",
            font=font.Font(size=28, weight="bold"),
        )
        self.display.pack()

    def _create_board_grid(self):
        """
        Creates a grid of buttons representing the game board.

        This function iterates over the board size to create a grid of buttons using Tkinter.
        Each button is configured with specific properties like text, font, color, and size.
        The buttons are then mapped to cell positions and bound to a play event.

        Parameters:
            self (TicTacToeBoard): The instance of the TicTacToeBoard class.

        Returns:
            None
        """
        grid_frame = tk.Frame(master=self)
        grid_frame.pack()
        for row in range(self._game.board_size):
            self.rowconfigure(row, weight=1, minsize=50)
            self.columnconfigure(row, weight=1, minsize=75)
            for col in range(self._game.board_size):
                button = tk.Button(
                    master=grid_frame,
                    text="",
                    font=font.Font(size=36, weight="bold"),
                    fg="black",
                    width=3,
                    height=2,
                    highlightbackground="lightblue",
                )
                self._cells[button] = (row, col)
                button.bind("<ButtonPress-1>", self.play)
                button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

    def play(self, event):
        """Handle a player's move."""
        clicked_btn = event.widget
        row, col = self._cells[clicked_btn]
        move = Move(row, col, self._game.current_player.label)
        if self._game.is_valid_move(move):
            self._update_button(clicked_btn)
            self._game.process_move(move)
            if self._game.is_tied():
                self._update_display(msg="Tied game!", color="red")
            elif self._game.has_winner():
                self._highlight_cells()
                msg = f'Player "{self._game.current_player.label}" won!'
                color = self._game.current_player.color
                self._update_display(msg, color)
            else:
                self._game.toggle_player()
                msg = f"{self._game.current_player.label}'s turn"
                self._update_display(msg)

    def _update_button(self, clicked_btn):
        """
        Update the appearance of the clicked button with the current player's label and color.

        Parameters:
            self (TicTacToeBoard): The instance of the TicTacToeBoard class.
            clicked_btn (Button): The button that was clicked and needs to be updated.

        Returns:
            None
        """
        clicked_btn.config(text=self._game.current_player.label)
        clicked_btn.config(fg=self._game.current_player.color)

    def _update_display(self, msg, color="black"):
        """
        Updates the display with the given message and color.

        Parameters:
            msg (str): The message to be displayed.
            color (str, optional): The color of the message. Defaults to "black".

        Returns:
            None
        """
        self.display["text"] = msg
        self.display["fg"] = color

    def _highlight_cells(self):
        """
        Highlight the cells that are part of the winning combination.

        Parameters:
            self (TicTacToeBoard): The instance of the TicTacToeBoard class.

        Returns:
            None
        """
        for button, coordinates in self._cells.items():
            if coordinates in self._game.winner_combo:
                button.config(highlightbackground="red")

    def reset_board(self):
        """Reset the game's board to play again."""
        self._game.reset_game()
        self._update_display(msg="Ready?")
        for button in self._cells.keys():
            button.config(highlightbackground="lightblue")
            button.config(text="")
            button.config(fg="black")


def ttt():
    """Create the game's board and run its main loop."""
    game = TicTacToeGame()
    board = TicTacToeBoard(game)
    board.mainloop()
