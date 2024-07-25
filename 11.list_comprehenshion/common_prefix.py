words = ["fly","float","flower","flat"]


smallest_word = min(words, key=len)

# for word in words:
    
#     if len(word) < length:
#         smallest_word = word
#         length = len(smallest_word)
        
for word in words:
    
    if smallest_word not in word:
        smallest_word = smallest_word[:-1]

print(smallest_word)