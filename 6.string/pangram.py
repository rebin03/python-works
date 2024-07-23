# pangram - the text which contains all the letters in aplphabet

text = "The Quick Brown Fox Jumps Over The Lazy Dog"

alphabets = "abcdefghijklmnopqrstuvwxyz"
text = text.casefold()
isPangram = True

for ch in alphabets:
    
    if text.count(ch) == 0:
        isPangram = False
        break
    
print(isPangram)