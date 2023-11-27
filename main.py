import random

def get_computer_choice(difficulty_level):
    if difficulty_level == "easy":
        return random.choice(["rock", "paper", "scissors"])
    elif difficulty_level == "medium":
        weighted_choices = ["rock"] * 5 + ["paper"] * 3 + ["scissors"] * 2
        return random.choice(weighted_choices)
    elif difficulty_level == "hard":
        weighted_choices = ["rock"] * 2 + ["paper"] * 3 + ["scissors"] * 5
        return random.choice(weighted_choices)
    else:  # difficulty level is expert
        weighted_choices = ["rock", "paper", "scissors"]
        return random.choices(weighted_choices, weights = [3, 4, 3])[0]

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        return "Player wins!"
    else:
        return "Computer wins!"

def play_game(difficulty_level):
    player_score = 0
    computer_score = 0
    tie_counter = 0
    score_increment = {"easy": 5, "medium": 10, "hard": 15, "expert": 20}

    while True:
        player_choice = input("Enter rock, paper, or scissors (or 'quit' to exit): ").lower()

        if player_choice == 'quit':
            break

        computer_choice = get_computer_choice(difficulty_level)
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
            break

    print("Game over!")
    print(f"Player score: {player_score}")
    print(f"Computer score: {computer_score}")

if __name__ == "__main__":
    difficulty_level = input("Choose your difficulty level (easy/medium/hard/expert): ")
    play_game(difficulty_level)