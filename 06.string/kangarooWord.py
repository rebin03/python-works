# A kangaroo word is “a word that contains its own synonym, with the letters to spell that synonym already placed in the correct order.

# Kangaroo word	    Joey word
# -----------------------------
# ravaging	        raging
# recline	        lie
# respite	        rest
# regulate	        rule

source_word = "listen"
target_word = "ten"
curr_index = 0

def is_kangaroo_word(source_word, target_word):
    j = 0
    count = 0
    for i in range(len(source_word)):
        if j < len(target_word):
            if source_word[i] == target_word[j]:
                count += 1
                j += 1
                
    return count == len(target_word)

print(is_kangaroo_word(source_word, target_word))
            
        
        
        
# print(is_kangaroo_word(source_word, target_word))