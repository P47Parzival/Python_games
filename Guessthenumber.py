import random

def guess_the_number():
    number = random.randint(1, 10)
    attempts = 0
    
    print("Welcome to 'Guess the Number' game!")
    
    while True:
        guess = input("Guess a number between 1 and 10: ")
        
        if not guess.isdigit():
            print("Please enter a valid number!")
            continue
        
        guess = int(guess)
        attempts += 1
        
        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts.")
            break

if __name__ == "__main__":
    guess_the_number()
