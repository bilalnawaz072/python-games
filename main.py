import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        return "Player wins!"
    else:
        return "Computer wins!"

def play_game():
    player_choice = input("Enter rock, paper, or scissors: ").lower()
    computer_choice = get_computer_choice()
    print(f"Computer chose {computer_choice}")
    result = determine_winner(player_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    play_game()
