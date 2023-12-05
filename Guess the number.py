import random

def select_difficulty():
    while True:
        difficulty = input("Choose your difficulty (easy/medium/hard): ").lower()
        if difficulty in ["easy", "medium", "hard"]:
            return difficulty
        else:
            print("Invalid input. Please enter 'easy', 'medium', or 'hard'.")

def get_num_tries(difficulty):
    if difficulty == "easy":
        return 12
    elif difficulty == "medium":
        return 8
    elif difficulty == "hard":
        return 4

def play_game(num_try, generated_num):
    while num_try > 0:
        try:
            user_guess = int(input("Enter your guess between 1 and 100: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if user_guess == generated_num:
            print(f"You have guessed the correct number: {generated_num}")
            return True
        else:
            num_try -= 1
            if user_guess < generated_num:
                print("Too low.")
            else:
                print("Too high.")
            if num_try > 0:
                print(f"You have {num_try} tries left.")
            else:
                print("You have lost. The correct number was:", generated_num)
                return False

def main():
    print("Welcome to the number guessing game!")
    print("Please select a difficulty option: 'easy', 'medium', or 'hard'.")
    play_again = True

    while play_again:
        difficulty = select_difficulty()
        num_try = get_num_tries(difficulty)
        print(f"You have selected {difficulty.capitalize()} difficulty and you have {num_try} tries.")
        generated_num = random.randint(1, 100)
        
        if play_game(num_try, generated_num):
            print("Congratulations! You won.")
        else:
            print("Better luck next time!")

        if input("Do you want to play again? (yes/no): ").lower() != "yes":
            play_again = False

if __name__ == "__main__":
    main()
