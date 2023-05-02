def game():
    import random

    player = int(input("Enter the number (0-9): "))
    options = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    computer = random.choice(options)

    if player > computer:
        print("You choose", player)
        print("Computer choose", computer)
        print("You Win!!")
    elif player < computer:
        print("You choose", player)
        print("Computer choose", computer)
        print("Compter Win")
    else:
        print("You choose", player)
        print("Computer choose", computer)
        print("It's a Tie")


ok = int(input("How many time you want to play: "))
i = 1
while i <= ok:
    game()
    i = i + 1