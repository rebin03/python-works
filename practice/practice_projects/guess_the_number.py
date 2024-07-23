import random
import logo_art

EASY_LEVEL = 10
HARD_LEVEL = 5

print(logo_art.logo)

def set_difficulty(level):
    if level == "easy":
        return EASY_LEVEL
    elif level == "hard":
        return HARD_LEVEL
    else:
        return

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
    
    if attempts != EASY_LEVEL and attempts != HARD_LEVEL:
        print("You have entered wrong difficulty...Play again!!")
        return
    
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