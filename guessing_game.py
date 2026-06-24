import random

def play_game():
    print("=================================")
    print("🎯 WELCOME TO THE NUMBER GUESSING GAME! 🎯")
    print("=================================")
    print("I'm thinking of a number between 1 and 100.")
    
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            # Get user input
            guess = int(input("\nEnter your guess: "))
            attempts += 1
            
            # Check the guess
            if guess < secret_number:
                print("📉 Too low! Try a higher number.")
            elif guess > secret_number:
                print("📈 Too high! Try a lower number.")
            else:
                print(f"\n🎉 CONGRATULATIONS! You guessed it in {attempts} attempts!")
                input("\nPress Enter to exit...")   
                break
        except ValueError:
            print("❌ Invalid input. Please enter a valid whole number.")

if __name__ == "__main__":
    play_game()
