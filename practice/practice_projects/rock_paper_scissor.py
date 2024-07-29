import logo_art, random

print(logo_art.logo1)

selection = {
    0:"Rock",
    1:"Paper",
    2:"Scissor"
}

user_input = int(input("0 for Rock\n1 for Paper\n2 for Scissor\n\nEnter number: "))
computer = random.randint(0,2)

print(f"\nyou: {selection.get(user_input)}\nSystem: {selection.get(computer)}\n")

if user_input == computer:
    print("Draw!!")
elif user_input == 0 and computer == 2:
    print("You win!")
elif user_input == 2 and computer == 0:
    print("You lose!")
elif computer > user_input:
    print("You lose!")
elif user_input > computer:
    print("You win!")
else:
    print("Invalid number")