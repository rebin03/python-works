import random
import logo_art

print(logo_art.logo)

def set_difficulty(level):
    return 10 if level == "easy" else 5

def check_answer(guessed_num, num, attempts):
    if guessed_num == num:
        print(f"Your guess is right... The answer was {num}")
        return
    elif guessed_num > num:
        print("Your guess is too high!")
        return attempts - 1
    else:
        print("Your guess is too low!")
        return attempts - 1


def guess_game():
    
    print("Let me think of a number berween 1-50.")
    num = random.randint(1,50)

    level = input("Choose the level of dificulty...Type 'easy' or 'hard': ")

    attempts = set_difficulty(level)
    
    guessed_num = 0
    while guessed_num != num:
        
        print(f"You have {attempts} attempt to guess the number!")
        guessed_num = int(input("Make a guess: "))
        
        attempts = check_answer(guessed_num, num, attempts)
        
        if attempts != 0:
            print("Guess again")
        elif guessed_num != num:
            print(f"You are out of guesses... You lose!!\nThe number is {num}")
            return

guess_game()