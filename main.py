from stone_paper import play_game

def main():
    while True:
        print("\n===== MAIN MENU =====")
        print("1. Play Stone Paper Scissors")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            play_game()
        elif choice == "2":
            print("Exiting game...")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()