import random

def guess_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Initialize the number of guesses
    guesses = 0
    
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Try to guess it.")
    
    while True:
        try:
            user_guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        guesses += 1
        
        if user_guess < secret_number:
            print("Too low! Try guessing higher.")
        elif user_guess > secret_number:
            print("Too high! Try guessing lower.")
        else:
            print(f"Congratulations! You've guessed the number in {guesses} tries.")
            break

if __name__ == "__main__":
    guess_number()
