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
    player_score = 0
    computer_score = 0
    
    while True:
        player_choice = input("Enter rock, paper, or scissors (or 'quit' to exit): ").lower()
        
        if player_choice == 'quit':
            break
        
        computer_choice = get_computer_choice()
        print(f"Computer chose {computer_choice}")
        result = determine_winner(player_choice, computer_choice)
        print(result)
        
        if result == "Player wins!":
            player_score += 1
            print(f"Current scores: Player : {player_score}, Computer : {computer_score}")
        elif result == "Computer wins!":
            computer_score += 1
            print(f"Current scores: Player : {player_score}, Computer : {computer_score}")
    
    print("Game over!")
    print(f"Player score: {player_score}")
    print(f"Computer score: {computer_score}")

if __name__ == "__main__":
    play_game()
