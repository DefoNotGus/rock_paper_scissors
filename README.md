# Rock Paper Scissors - Guided Tutorial

Welcome to the **Rock Paper Scissors** guided tutorial! 🎮 This project is designed to help you learn Python while implementing a fun and interactive game. You'll be provided with `main.py`, which is a partially completed program that you will enhance.

## Features
The program will allow you to:
1. Let the user choose a tool (**Rock**, **Paper**, or **Scissors**).
2. Make the computer randomly choose a tool.
3. Determine the winner based on the game rules.

## Instructions
### Implementing the `determine_winner` Function
This guide will help you implement the `determine_winner` function in a few simple steps.

### Steps to Implement `determine_winner`

#### 1. Define the Function
Create a function called `determine_winner` that takes two arguments: `user` and `computer`.
```python
def determine_winner(user, computer):
```

#### 2. Print Choices for Clarity
Inside the function, print both the user’s choice and the computer’s choice.
```python
    print(f"You chose: {user}")
    print(f"Computer chose: {computer}")
```

#### 3. Handle the Case of a Tie
If both choices are the same, return a message indicating a tie.
```python
    if user == computer:
        return "It's a tie!"
```

#### 4. Define Winning Conditions
Use `if` statements to check if the user wins.
```python
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "You win! 🎉"
```

#### 5. Handle the Case Where the Computer Wins
If none of the winning conditions are met, return that the computer wins.
```python
    else:
        return "Computer wins! 🤖"
```

#### 6. Integrate the Function into `play_game`
Call `determine_winner` inside `play_game` and print the result.
```python
    result = determine_winner(user_choice, computer_choice)
    print(result)
```

#### 7. Test the Function
Run the script multiple times and try different inputs (**rock**, **paper**, **scissors**) to ensure it works correctly.

#### 8. Add More Features (Optional)
- Keep track of the score.
- Allow the user to play multiple rounds.
- Add more fun responses for wins and losses!

### Bonus Task 🎯
Modify the program to make it **impossible** to win! Instead of making the computer choose randomly, simply print a message saying that the computer always picks the winning tool.

Example:
```python
    if user == "Scissors"
    print("Computer chose rock. You lose! 🤖")
```

Now prank your friends to play it!

