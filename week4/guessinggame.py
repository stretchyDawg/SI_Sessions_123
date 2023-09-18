import random

def check_number(guess, answer):
    if guess == answer:
        return "Correct. You win!"
    if guess > answer:
        return "Too high!"
    if guess < answer:
        return "Too low!"
    return None

def guessing_game():
    answer = random.randint(1, 100)

    guess1 = int(input("Enter a number: "))
    if check_number(guess1, answer) == "Correct. You win!":
        return "Correct. You win!"
    print(check_number(guess1, answer))
    
    guess2 = int(input("Enter a number: "))
    if check_number(guess2, answer) == "Correct. You win!":
        return "Correct. You win!"
    print(check_number(guess2, answer))

    guess3 = int(input("Enter a number: "))
    if check_number(guess3, answer) == "Correct. You win!":
        return "Correct. You win!"
    print(check_number(guess3, answer))

    guess4 = int(input("Enter a number: "))
    if check_number(guess4, answer) == "Correct. You win!":
        return "Correct. You win!"
    print(check_number(guess4, answer))

    guess5 = int(input("Enter a number: "))
    if check_number(guess5, answer) == "Correct. You win!":
        return "Correct. You win!"
    print(check_number(guess5, answer))

    guess6 = int(input("Enter a number: "))
    if check_number(guess6, answer) == "Correct. You win!":
        return "Correct. You win!"
    print(check_number(guess6, answer))

    print("Out of guesses!")

def main():
    guessing_game()

main()
