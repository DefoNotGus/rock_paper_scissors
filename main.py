'''
YOU ONLY HAVE TO INSERT THE CODE STARTING FROM LINE 23
DO NOT CHANGE ANYTHING ELSE 
'''
import random

# Function to get the computer's random choice
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

# Function to get the user's choice, ensuring it's valid
def get_user_choice():
    choice = input("Choose rock, paper, or scissors: ").lower()
    while choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Try again!")
        choice = input("Choose rock, paper, or scissors: ").lower()
    return choice

# Function to play the game
def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    
    # TODO: Implement determine_winner function here


    #! when you reach stage 6 delete the '#' before the lines below
    # result = determine_winner(user_choice, computer_choice)
    # print(result)
    
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    print("AND WHAT NOW...?")

if __name__ == "__main__":
    play_game()