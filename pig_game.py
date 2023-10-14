from random import randint


def roll():
    roll = randint(1, 6)
    return roll


def play_game():
    while True:
        try:
            players_count = int(input("Enter the number of players (1-4): "))

            if players_count not in range(1, 5):
                print("Invalid option. Enter the number of players (1-4): ")

            else:
                break
        except ValueError:
            print("Invalid option. Enter the number of players (1-4): ")

    current_score = 0
    players = [0] * players_count
    while True:
        try:
            max_score = int(input("What should the max score be?: "))
            if max_score <= 0:
                print("Invalid option. Max score should be greater than 0.")
            else:
                break
        except ValueError:
            print("Invalid option.")
    print(players)
    while max(players) < max_score:
        possible_moves = ["roll", "hold"]
        for index in range(len(players)):
            print(f"Player {index + 1} turn\n")
            while True:
                player_move = input("Do you want to roll or hold?\n").lower()

                if player_move not in possible_moves:
                    print("Possible moves are roll and hold")
                elif player_move == possible_moves[0]:
                    rolled = roll()
                    if rolled == 1:
                        print("You lost the streak :(\n"
                              "Score: 0\n")
                        current_score = 0
                        break
                    else:
                        current_score += rolled
                        print(f"\nYou got {rolled}!")
                        print(f"Current streak: {current_score}")
                        print(f"Score: {players[index]}\n")
                elif player_move == possible_moves[1]:
                    players[index] += current_score
                    current_score = 0
                    print(f"Player {index + 1} chose to hold.\n"
                          f"Scores: {players}")
                    break

    max_score = max(players)
    win_idx = players.index(max_score)
    print(f"Player {win_idx} won!")


while True:
    play_game()

    play_again = input("Would you like to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break
