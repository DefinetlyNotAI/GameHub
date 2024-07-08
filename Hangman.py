import random

HANGMAN_PICS = [
    r"""
   +---+
       |
       |
       |
      ===""",
    r"""
   +---+
   O   |
       |
       |
      ===""",
    r"""
   +---+
   O   |
   |   |
       |
      ===""",
    r"""
   +---+
   O   |
  /|   |
       |
      ===""",
    r"""
   +---+
   O   |
  /|\  |
       |
      ===""",
    r"""
   +---+
   O   |
  /|\  |
  /    |
      ===""",
    r"""
   +---+
   O   |
  /|\  |
  / \  |
      ===""",
]

words = "ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra".split()


def getRandomWord(wordList):
    """
    Returns a random word from the given word list.

    Parameters:
        wordList (list): A list of words.

    Returns:
        str: A randomly selected word from the word list.
    """
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]


def displayBoard(missedLetters, correctLetters, secretWord):
    """
    Display the hangman game board with the missed letters, correctly guessed letters, and the secret word.

    Parameters:
        missedLetters (str): A string of letters that have been guessed incorrectly.
        correctLetters (str): A string of letters that have been guessed correctly.
        secretWord (str): The secret word being guessed.

    Returns:
        None
    """
    print(HANGMAN_PICS[len(missedLetters)])
    print()
    print("Missed letters:", end=" ")
    for letter in missedLetters:
        print(letter, end=" ")
    print()
    blanks = "_" * len(secretWord)

    for i in range(len(secretWord)):  # Replace blanks with correctly guessed letters.
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i + 1 :]

    for letter in blanks:  # Show the secret word with spaces in between each letter.
        print(letter, end=" ")
    print()


def getGuess(alreadyGuessed):
    """
    Prompts the user to guess a letter until a valid input is provided.

    Parameters:
        alreadyGuessed (str): A string of letters that have already been guessed.

    Returns:
        str: A lowercase letter that the user has guessed.

    Raises:
        None

    This function prompts the user to guess a letter until a valid input is provided. It takes in a list of letters
    that have already been guessed. The function continues to prompt the user until they enter a single lowercase
    letter that has not already been guessed. If the user enters a letter that is not a single lowercase letter,
    the function displays an error message and prompts the user again. The function returns the valid guessed letter.
    """
    while True:
        print("Guess a letter.")
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print("Please enter a single letter.")
        elif guess in alreadyGuessed:
            print("You have already guessed that letter. Choose again.")
        elif guess not in "abcdefghijklmnopqrstuvwxyz":
            print("Please enter a LETTER.")
        else:
            return guess


def playAgain():
    """
    Asks the user if they want to play again. Returns True if the user wants to play again, False otherwise.
    """
    print("Do you want to play again? (yes or no)")
    return input().lower().startswith("y")


def Hangman_game():
    """
    A simple Hangman game function that allows players to guess letters until they either win or lose.
    It initializes the game settings, displays the board, takes guesses, checks for correct guesses, updates missed letters, and handles game outcomes.
    The game continues until the player chooses to stop or finishes the game.
    """
    print("H A N G M A N")
    missedLetters = ""
    correctLetters = ""
    secretWord = getRandomWord(words)
    gameIsDone = False
    print("To exit the game type 'exit()'")

    while True:
        displayBoard(missedLetters, correctLetters, secretWord)
        guess = getGuess(missedLetters + correctLetters)

        if guess == "exit()":
            print("Thanks for playing!")
            exit(0)

        if guess in secretWord:
            correctLetters += guess

            # Check if the player has won.
            foundAllLetters = True
            for i in range(len(secretWord)):
                if secretWord[i] not in correctLetters:
                    foundAllLetters = False
                    break
            if foundAllLetters:
                print('Yes! The secret word is "' + secretWord + '"! You have won!')
                gameIsDone = True
        else:
            missedLetters += guess

            # Check if player has guessed too many times and lost.
            if len(missedLetters) == len(HANGMAN_PICS) - 1:
                displayBoard(missedLetters, correctLetters, secretWord)
                print(
                    "You have run out of guesses!\nAfter "
                    + str(len(missedLetters))
                    + " missed guesses and "
                    + str(len(correctLetters))
                    + ' correct guesses, the word was "'
                    + secretWord
                    + '"'
                )
                gameIsDone = True

        # Ask the player if they want to play again (but only if the game is done).
        if gameIsDone:
            if playAgain():
                missedLetters = ""
                correctLetters = ""
                gameIsDone = False
                secretWord = getRandomWord(words)
            else:
                break
