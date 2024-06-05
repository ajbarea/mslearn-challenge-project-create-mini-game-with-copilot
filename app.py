# Rock Paper Scissors App

# The winner of the game is determined by three simple rules:
# 1. Rock beats scissors.
# 2. Scissors beat paper.
# 3. Paper beats rock.

# The computer will be the Users opponent and can randomly choose one of the elements (rock, paper, or scissors) for each move, just like the User.
# The interactions in the game will be through the console.
# The player can choose one of the three options rock, paper, or scissors and should be warned if they enter an invalid option.
# At each round, the player must enter one of the options in the list and be informed if they won, lost, or tied with the opponent.
# By the end of each round, the player can choose whether to play again.
# Display the player's score at the end of the game.
# The minigame must handle user inputs, putting them in lowercase and informing the user if the option is invalid.

# Importing the random module
import random

def display_welcome_message():
    welcome_message = """
    Welcome to the Rock, Paper, Scissors Game!

    The winner of each round is determined by three simple rules:
        1. Rock beats Scissors.
        2. Scissors beat Paper.
        3. Paper beats Rock.

    How to play:
    - You can choose one of the three options: rock, paper, or scissors.
    - If you enter an invalid option, you will be warned.

    Each round, enter one of the options and you will be informed if you won, lost, or tied with your opponent.

    Let the games commence!
    """
    print(welcome_message)

# Defining the main function of the game
def rock_paper_scissors():
    # Defining the options for the game
    options = ["rock", "paper", "scissors"]
    # Defining the player's score
    player_score = 0
    # Defining the computer's score
    computer_score = 0

    # Call the function to display the welcome message
    display_welcome_message()

    # Defining the game loop
    while True:
        # Getting the player's move
        player_move = input("\nEnter your move (rock, paper, or scissors): ").lower()
        # Validating the player's move
        while player_move not in options:
            print("Invalid option! Please enter a valid move.")
            player_move = input("\nEnter your move (rock, paper, or scissors): ").lower()

        # Getting the computer's move
        computer_move = random.choice(options)
        # Displaying the player's move
        print("You chose:", player_move)
        # Displaying the computer's move
        print("Opponent chose:", computer_move)

        # Determining the winner of the game
        if player_move == computer_move:
            print("It's a tie!")
        elif (player_move == "rock" and computer_move == "scissors") or (player_move == "scissors" and computer_move == "paper") or (player_move == "paper" and computer_move == "rock"):
            print("You won!")
            player_score += 1
        else:
            print("You lost!")
            computer_score += 1

        # Asking the player if they want to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        # Validating the player's choice
        while play_again not in ["yes", "no"]:
            print("Invalid option! Please enter a valid choice.")
            play_again = input("Do you want to play again? (yes/no): ").lower()
        # Checking if the player wants to play again
        if play_again == "no":
            print("Thank you for playing the Rock, Paper, Scissors game!")
            # Displaying the player's score
            print("FINAL SCORES:")
            print("Your score:", player_score)
            # Displaying the computer's score
            print("Computer's score:", computer_score)
            break
        
# Calling the main function of the game
rock_paper_scissors()