import random

def get_computer_choice():
    return random.choice(["stone", "paper", "scissors"])

def check_winner(user, comp):
    if user == comp:
        return "Draw"
    elif (user == "stone" and comp == "scissors") or \
         (user == "paper" and comp == "stone") or \
         (user == "scissors" and comp == "paper"):
        return "You Win!"
    else:
        return "Computer Wins!"

def play_game():  # Main Function where everything runs
    user_score = 0
    comp_score = 0

    while True:
        print("\n--- Stone Paper Scissors ---")
        print("1. Play Round")
        print("2. Back to Main Menu")

        choice = input("Enter choice: ")

        if choice == "2":
            break

        elif choice == "1":
            user = input("Enter stone/paper/scissors: ").lower()

            if user not in ["stone", "paper", "scissors"]:
                print("Invalid input!")
                continue

            comp = get_computer_choice()

            print("Computer chose:", comp)
            result = check_winner(user, comp)

            print("Result:", result)

            # UPDATE SCORE
            if result == "You Win!":
                user_score += 1
            elif result == "Computer Wins!":
                comp_score += 1

            print("Score -> You:", user_score, "| Computer:", comp_score)

        else:
            print("Invalid choice!")