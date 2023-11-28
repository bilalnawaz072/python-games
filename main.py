import random
import time

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)


def determine_winner(player_choice, computer_choice):
    win_conditions = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }

    if player_choice == computer_choice:
        return "It's a tie!"
    elif win_conditions[player_choice] == computer_choice:
        return "Player wins!"
    else:
        return "Computer wins!"

def play_game(difficulty_level):
    player_score = 0
    computer_score = 0
    tie_counter = 0
    score_increment = {"easy": 5, "medium": 10, "hard": 15, "expert": 20}
    overall_winner = None

    while True:
        start_time = time.time()
        player_choice = input("Enter rock, paper, or scissors (or 'quit' to exit): ").lower()

        elapsed_time = time.time() - start_time

        if elapsed_time > 10:
            print("Time limit exceeded. Quitting game...")
            print(f"Final scores: Player : {player_score}, Computer : {computer_score}")
            break

        if player_choice == 'quit':
            break

        computer_choice = get_computer_choice()
        print(f"Computer chose {computer_choice}")
        result = determine_winner(player_choice, computer_choice)
        print(result)

        if result == "Player wins!":
            player_score += score_increment[difficulty_level]
            print(f"Current scores: Player : {player_score}, Computer : {computer_score}")
        elif result == "Computer wins!":
            computer_score += score_increment[difficulty_level]
            print(f"Current scores: Player : {player_score}, Computer : {computer_score}")
        elif result == "It's a tie!":
            tie_counter += 1
            player_score += score_increment[difficulty_level] 
            computer_score += score_increment[difficulty_level] 
            print(f"Current scores: Player : {player_score}, Computer : {computer_score}")

        if tie_counter == 3:
            print("It has been a tie 3 times.Quitting game...")
            print("Game over!")
            print(f"Player score: {player_score}")
            print(f"Computer score: {computer_score}")
            break

        if player_score >= 50 and player_score > computer_score:
            print("Player wins the overall game!")
            overall_winner = "Player"
            break
        elif computer_score >= 50 and computer_score > player_score:
            print("Computer wins the overall game!")
            overall_winner = "Computer"
            break
        elif player_score == computer_score:
            print("TNo overall winner!")
            overall_winner = "Tie"
            break

   

if __name__ == "__main__":
    difficulty_level = input("Choose your difficulty level (easy/medium/hard/expert): ")
    play_game(difficulty_level)
