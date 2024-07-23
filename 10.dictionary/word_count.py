words = ["hello","hai","hello","hai","hai","hi"]

word_count = {}

for w in words:
    
    if w in word_count:
        
        word_count[w] += 1
    
    else:
        
        word_count[w] = 1

print(word_count)






# another method
# ---------------------------
# new_word = list(set(words))
# print(new_word)

# for word in new_word:
#     count = words.count(word)
#     print(f"{word}: {count}")

