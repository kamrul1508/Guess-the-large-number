ask_name = input("Enter Your Name: ")
print(f"Welome to the quiz game '{ask_name}'")

permission = input(f"Do you want to continue {ask_name}? (y/n) ")

if permission.lower() != "y":
    quit()

print("Okay! Let's play :)")

score = 0

answer = input("Q1: 2 + 2? ")
if answer == "4":
    print("Correct")
    score += 1
else:
    print("Sorry, You are wrong")


answer = input("Q1: 10 * 9? ")
if answer == "90":
    print("Correct")
    score += 1
else:
    print("Sorry, You are wrong")

answer = input("Q1: 3 * 5? ")
if answer == "15":
    print("Correct")
    score += 1
else:
    print("Sorry, You are wrong")

answer = input("Q1: 9 / 3? ")
if answer == "3":
    print("Correct")
    score += 1
else:
    print("Sorry, You are wrong")

answer = input("Q1: 45 - 15? ")
if answer == "30":
    print("Correct")
    score += 1
else:
    print("Sorry, You are wrong")

answer = input("Q1: 9 * 9? ")
if answer == "81":
    print("Correct")
    score += 1
else:
    print("Sorry, You are wrong")

if score == 0:
    print(f"Your score is {score}")
    print("Try Harder")
elif score <=2:
    print(f"Your score is {score}")
    print("Focus on Math more")

elif score <=4:
    print(f"Your score is {score}")
    print("Good")
else:
    print(f"Your score is {score}")
    print("Perfect!")