# Create Rock Paper Scissors game
# The computer will randomly choose rock, paper or scissors
# The user will choose rock, paper or scissors
# The computer will print out the result
import random

def StartGame():
    print("Welcome to Rock Paper Scissors")
    print("The computer will randomly choose rock, paper or scissors")
    print("The user will choose rock, paper or scissors")
    print("The computer will print out the result")
    print()

def GetUserChoice():
    user_choice = input("Please choose rock, paper or scissors: ")
    return user_choice

def GetComputerChoice():
    computer_choice = random.randint(1,3)
    if computer_choice == 1:
        computer_choice = "rock"
    elif computer_choice == 2:
        computer_choice = "paper"
    else:
        computer_choice = "scissors"
    print("The computer chose: " + computer_choice)
    return computer_choice


# Declared the wins
player_wins = 0
computer_wins = 0

# Get the choices
player_choice = GetUserChoice()
computer_choice = GetComputerChoice()


game_isactive = True

while game_isactive:
    if player_choice == computer_choice:
        print("It's a tie!")

    elif player_choice == "r":
        if computer_choice == "p":
            computer_wins += 1
            print("Computer wins!")
        else:
            player_wins += 1
            print("Player wins!")

    elif player_choice == "p":
        if computer_choice == "s":
            computer_wins += 1
            print("Computer wins!")
        else:
            player_wins += 1
            print("Player wins!")

    elif player_choice == "s":
        if computer_choice == "r":
            computer_wins += 1
            print("Computer wins!")
        else:
            player_wins += 1
            print("Player wins!")
            
    else:
        print("Invalid input!")


    print("Player wins: ", player_wins)
    print("Computer wins: ", computer_wins)
    print()

    if player_wins == 3:
        print("Player wins the game!")
        game_isactive = False
        break
    elif computer_wins == 3:
        print("Computer wins the game!")
        game_isactive = False
        break
    else:
        player_choice = GetUserChoice()
        computer_choice = GetComputerChoice()

    

    