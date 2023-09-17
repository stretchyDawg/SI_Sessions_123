"""
A guessing game; the user must guess a number from 1-10, they have three tries.
@ChristianMorgado
"""

import random
ANSWER = random.randint(1, 10)

def check_guess(answer, guess):
    """
    Checks if the guess made by the user is in range, too low, too high, or the correct answer. 
    """
    
    if guess < 1:
        return "Guess out of range!"

    if guess > 10:
        return "Guess out of range!"

    if guess < answer:
        return "Too low!"

    if guess > answer:
        return "Too high!"

    if guess == answer:
        return "Correct!"

def main():
    guess = int(input("Enter guess: "))
    outcome = check_guess(ANSWER, guess)
    print(outcome)

    if outcome != "Correct!":
        guess = int(input("Enter guess: "))
        outcome = check_guess(ANSWER, guess)
        print(outcome)

    if outcome != "Correct!":
        guess = int(input("Enter guess: "))
        outcome = check_guess(ANSWER, guess)
        print(outcome)

    if outcome != "Correct!":
        print("The answer was ", ANSWER, "!", sep = "")

    print("Game over!")

# main()





