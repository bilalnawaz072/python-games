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
    tie_counter = 0

    while True:
        player_choice = input("Enter rock, paper, or scissors (or 'quit' to exit): ").lower()
        
        if player_choice == 'quit':
            break
        
        computer_choice = get_computer_choice()
        print(f"Computer chose {computer_choice}")
        result = determine_winner(player_choice, computer_choice)
        print(result)
        
        if result == "Player wins!":
            player_score += 10
            print(f"Current scores: Player : {player_score}, Computer : {computer_score}")
        elif result == "Computer wins!":
            computer_score += 10
            print(f"Current scores: Player : {player_score}, Computer : {computer_score}")
        elif result == "It's a tie!":
            tie_counter += 1
            player_score += 5
            computer_score += 5
            print(f"Current scores: Player : {player_score}, Computer : {computer_score}")
        
        if tie_counter == 3:
            print("It has been a tie 3 times.Quitting game...")
            break
    
    print("Game over!")
    print(f"Player score: {player_score}")
    print(f"Computer score: {computer_score}")

if __name__ == "__main__":
    play_game()
