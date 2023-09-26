import random

rock = "Rock"
paper = "Paper"
scissors = "Scissors"
computer_move = ""
result = ""
games_count = int(input())
computer_wins = 0
player_wins = 0
again = input("Type [yes to play or [no] to quit: ")
while again == "yes":
    for i in range(games_count):
        player_move = input("Choose [r]ock, [p]aper or [s]cissors: ")
        if player_move == "r":
            player_move = rock
        elif player_move == "p":
            player_move = paper
        elif player_move == "s":
            player_move = scissors
        else:
            raise SystemExit("Invalid Input. Try again...")

        random_computer_number = random.randint(1, 3)

        if random_computer_number == 1:
            computer_move = rock
        elif random_computer_number == 2:
            computer_move = paper
        else:
            computer_move = scissors

        print(f"The computer chose {computer_move}.")

        if (player_move == rock and computer_move == scissors) or \
                (player_move == scissors and computer_move == paper) or \
                (player_move == paper and computer_move == rock):
            result = "You win!"
            player_wins += 1
        elif player_move == computer_move:
            result = "Draw!"
            player_wins += 1
            computer_wins += 1
        else:
            result = "You lose!"
            computer_wins += 1

        print(result)

    print(f"The final score is: player - {player_wins}, computer - {computer_wins}")

    if player_wins > computer_wins:
        print("The new winner is: Player")
    elif computer_wins > player_wins:
        print("The new winner is: Computer")
    else:
        print("Draw! Play again!")
    again = input("Type [yes to play again or [no] to quit: ")
