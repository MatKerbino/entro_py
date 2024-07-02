import random

exit = False
User_points = 0
Computer_points = 0

while not exit:
    options = ["rock", "paper", "scissors"]
    user_input = input("Choose rock, paper, scissors: ").lower()
    computer_input = random.choice(options)

    if user_input == "":
        print("Game End")
        print("You scored: {} Computer Scored: {}".format(User_points, Computer_points))
        exit = True

    if user_input == "rock":
        if computer_input == "rock":
            print("Your input is rock")
            print("Computer input is rock")
            print("It is a tie!")
        elif computer_input == "paper":
            print("Your input is Rock")
            print("Computer input is paper")
            print("Computer wins!")
            Computer_points += 1
        elif computer_input == "scissors":
            print("Your input is Rock")
            print("Computer input is scissors")
            print("You win!")
            User_points += 1

    if user_input == "paper":
        if computer_input == "rock":
            print("Your input is paper")
            print("Computer input is rock")
            print("You win!")
            User_points += 1
        elif computer_input == "paper":
            print("Your input is paper")
            print("Computer input is paper")
            print("Its a tie!")
        elif computer_input == "scissors":
            print("Your input is paper")
            print("Computer input is scissors")
            print("Computer wins!")
            Computer_points += 1

    if user_input == "scissors":
        if computer_input == "rock":
            print("Your input is scissors")
            print("Computer input is rock")
            print("Computer Wins!")
            Computer_points += 1
        elif computer_input == "paper":
            print("Your input is scissors")
            print("Computer input is paper")
            print("You win!")
            User_points += 1
        elif computer_input == "scissors":
            print("Your input is Scissors")
            print("Computer input is scissors")
            print("ITS A TIE!")




