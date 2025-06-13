import random

computer = random.randint(1, 3)

print("1) ✊")
print("2) ✋")
print("3) ✌️")

player = int(input("Select a number between 1 and 3: "))

def yourGame():
    if player < 1 or player > 3:
        print("Invalid input")
    elif player == 1 and computer == 2 or player == 2 and computer == 3 or player == 3 and computer == 1:
        print("You lose!")
        print("Computer chose", computer)
    elif player == 1 and computer == 3 or player == 2 and computer == 1 or player == 3 and computer == 2:
        print("You win!")
        print("Computer chose", computer)
    elif player == computer:
        print("Repeat!")
        print("Computer chose", computer)

yourGame()