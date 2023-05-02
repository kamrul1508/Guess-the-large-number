def calculator(num1, num2):
    user_input = input("Enter the Expression you want to perform (+, -, *, /) & Type 'end' to terminate: ")
    if user_input == "+":
        sun = num1 + num2
        print("This is your result", sun)
    elif user_input == "-":
        sun = num1 - num2
        print("This is your result", sun)
    elif user_input == "*":
        sun = num1 * num2
        print("This is your result", sun)
    elif user_input == "/":
        sun = num1 / num2
        print("This is your result", sun)
    elif user_input == "end":
        quit()
    else:
        print("Please Enter the right expression!")


i = 1
while i <= 100:
    calculator(int(input("Enter the 1st number: ")), int(input("Enter the 2nd number: ")))
    print("Calculation Number ", i)
    i += 1
