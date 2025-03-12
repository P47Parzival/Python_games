# computer = -1
# youstr = input("Enter your choice: ")
# yourdict = {"s": 1, "w": -1, "g": 0}
# you = yourdict[youstr]

# if(computer == -1 and you == 1):
#     print("You Win!")
# elif(computer == -1 and you == 0):
#     print("You Lose!")

# elif(computer == 1 and you == 0):
#     print("You Win!")
# elif(computer == 1 and you == -1):
#     print("You Lose!")

# elif(computer == 0 and you == -1):
#     print("You Win!")
# elif(computer == 0 and you == 1):
#     print("You Lose!")

# else:
#     print("Print somethin went wrong")


import random

computer_choices = {"s": 1, "w": -1, "g": 0}
computer = random.choice(list(computer_choices.values()))

youstr = input("Enter your choice (s for snake, w for water, g for gun): ").lower()
yourdict = {"s": 1, "w": -1, "g": 0}

if youstr not in yourdict:
    print("Invalid choice! Please enter 's', 'w', or 'g'.")
else:
    you = yourdict[youstr]

    if computer == you:
        print("It's a tie!")
    elif (computer == -1 and you == 1) or (computer == 1 and you == 0) or (computer == 0 and you == -1):
        print("You Win!")
    else:
        print("You Lose!")

    computer_choice_str = [k for k, v in computer_choices.items() if v == computer][0]
    print(f"Computer chose: {computer_choice_str}")
    print(f"You chose: {youstr}")