speed = input("Enter The Speed in Km/h: ")
speed = int(speed)

if speed < 60:
    print(f"Your speed was {speed} and you are good to go")

else:
    if speed <= 60:
        print("You are going perfect!")

    elif speed >= 61 and speed <= 90:
        new_speed = int(speed - 60)
        fine = 50 + (new_speed * 5)
        print(f"Your Speed was {speed} and Your fine is {fine}")

    elif speed > 90:
        new_speed = int(speed - 60)
        print(new_speed)
        fine = 200 + 50 + (new_speed * 5)
        print(f"Your Speed was {speed} and Your fine is {fine}")
