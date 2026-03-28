import random

def number_guessing_game():
    print("🎮 Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")

    number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number:
                print("📉 Too low! Try again.")
            elif guess > number:
                print("📈 Too high! Try again.")
            else:
                print(f"🎉 Congratulations! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("⚠️ Please enter a valid number!")

    print("Thanks for playing! 😊")

# Run the game
if __name__ == "__main__":
    number_guessing_game()
