import random


def get_choices():
    player_choice = input("Enter a Choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices


def check_win(player, computer):
    print(f"You choose {player}, Computer Choose {computer}")
    if player == computer:
        return "it's a tie"

    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You Win!"
        else:
            return "Papers Cover Rock! You Loose. Better luck next time!"
    elif player == "paper":
        if computer == "rock":
            return "Papers Cover Rock! You Win!"
        else:
            return "Scissors cuts paper! You Loose. Better luck next time!"
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cuts paper! You Win!"
        else:
            return "Rock smashes scissors! You Loose. Better luck next time!"


choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
