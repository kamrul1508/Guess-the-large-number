import random

top_of_range = int(input("Type a number: "))

if top_of_range <= 0:
    print("Please type a larger number then 0 next time")
    quit()

print(f"Congratulations you choose {top_of_range}.")
print(f"Yoyr range is 1 - {top_of_range}")

random_number = random.randint(1, top_of_range)
guess_number = 0
while True:
    guess_number += 1
    user_guess = int(input("Enter a Number: "))
    if user_guess == random_number:
        print("You Got it Right!")
        print(f"You got it in {guess_number} guess. Better luck nect time")
        quit()
    elif user_guess > random_number:
        print("You are above the number!")
    else:
        print("You are below the number!")
