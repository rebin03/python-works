words = ["hello","hai","python","apple","eagle"]
vowels = ["A","E","I","O","U","a","e","i","o","u"]

for i in range(0,len(words)):
    for j in vowels:
        if words[i].startswith(j):
            print(words[i])