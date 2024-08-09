import random
import man

print(man.logo)

print("Let's Play Hangman!!")
print("You have only 6 lives, So try to guess the word within 6 attempts! Good luck!!")

words = ["apple", "vehicle", "school", "python", "program", "laptop", "icecream","Tiger"]

guessing_word = random.choice(words).lower()
og_word = list(guessing_word)

filling_list = ["_"]*len(guessing_word)
print(filling_list)

guess = 6

while guess != 0:
    guessed_letter = input("Guess a letter: ").lower()
    
    if guessed_letter not in og_word:
        print(f"You guessed {guessed_letter} that is not present in the word. So you lose a life")
        guess -= 1
        if guess == 0:
            print(man.lose)
            print(f"The word is '{guessing_word}'")
    else:
        for i in range(len(og_word)):
            if og_word[i] == guessed_letter:
                filling_list[i] = guessed_letter
                og_word[i] = "_"
                
    print(filling_list)
    
    if "".join(filling_list) == guessing_word:
        print(man.win)
        print(hang_man_list[guess])
        guess = 0
        break
        
    hang_man_list = man.hanging
    
    print(hang_man_list[guess])