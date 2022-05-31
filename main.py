import random

possible_options = ["rock", "paper", "scissors"]


def computer_choice():
    comp_choice = random.choice(possible_options)
    return comp_choice


def player_choice():
    player = input("Choose between Rock, Paper, Scissors: \n").lower()
    return player

def game(computer, player):
    winner = False
    
    print(f'Player {player} :  CPU {computer}')
    
    if player == "rock":
        if computer == "scissors":
            print("You win")
            winner = True
            
        elif computer == "paper":
            print("You lose")
            winner = True
        else:
            print("it is a tie")
    elif player == "paper":
        if computer == "rock":
            print("You win")
            winner = True
            
        elif computer == "scissors":
            print("You lose")
            winner = True
        else:
            print("it is a tie")
    else:
        if player == "scissors":
            if computer == "paper":
                print("You win")
                winner = True
                
            elif computer == "rock":
                print("You lose")
                winner = True
            else:
                print('it is a tie')
    return winner


found_winner = False

while not found_winner:

    player = player_choice()
    computer = computer_choice()

    game_result = game(computer, player)
    
    if game_result == True:
        found_winner = True
        break