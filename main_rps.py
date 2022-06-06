#this is a program for determining the winner in rock, paper,scissors game

import random

def rps(computer_player,personal_player1):

    while True:
        options = ["rock","paper","scissors"]

        computer_player = random.choice(options)
        personal_player1 = None

        while personal_player1 not in options:

            personal_player1 = input("rock, paper, or scissors?: ").lower()

        if personal_player1 == computer_player:
            print("You chose ", personal_player1, " and computer player chose ", computer_player)
            print("It is a Tie")
        elif personal_player1 == "rock":
            if computer_player == "paper":
                print("You chose ", personal_player1, " and computer player chose ", computer_player)
                print("player wins!!, Rock beats paper")
            if computer_player == "scissors":
                print("You chose ", personal_player1, " and computer player chose ", computer_player)
                print("player lose, Rock cannot beat scissors")

        elif personal_player1 == "paper":
            if computer_player == "rock":
                print("You chose", personal_player1, " and computer player chose ", computer_player)
                print("player loss, paper cannot beats Rock")
            if computer_player == "scissors":
                print("You chose ", personal_player1, " and computer player chose ", computer_player)
                print("player lose, Rock cannot beat scissors")

        elif personal_player1 == "scissors":
            if computer_player == "paper":
                print("You chose ", personal_player1, " and computer player chose ", computer_player)
                print("player wins!!, Scissors beats paper")
            if computer_player == "rock":
                print("You chose ", personal_player1, " and computer player chose ", computer_player)
                print("player lose, Rock cannot beat scissors")

        try_again = input("Do you want to Play again? \n (yes/no)").lower()
        if try_again != "yes":
            break
    return "See You later!"

players = rps(computer_player="rock", personal_player1="rock")
print(players)
