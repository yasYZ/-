import random

def get_user_choice():
    choice = input("Choose your option (rock, paper, or gheychi): ")
    while choice.lower() not in ["rock", "paper", "gheychi"]:
        print("Invalid choice. Please choose again.")
        choice = input("Choose your option (rock, paper, or gheychi): ")
    return choice.lower()

def get_computer_choice():
    choices = ["rock", "paper", "gheychi"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!", 0
    elif (user_choice == "rock" and computer_choice == "gheychi") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "gheychi" and computer_choice == "paper"):
        return "You win!", 1
    else:
        return "Computer wins.", -1

def play_game():
    print("Rock, Paper, gheychi Game")
    print("please write finglish")
    print("-------------------------")
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print("You chose:", user_choice)
        print("Computer chose:", computer_choice)
        winner, score = determine_winner(user_choice, computer_choice)
        user_score += score
        computer_score -= score
        print(winner)
        print("Your score:", user_score)
        print("Computer's score:", computer_score)
        print("-------------------------")
        play_again = input("Do you want to continue? (yes/no): ")
        if play_again.lower() != "yes":
            break

play_game()
