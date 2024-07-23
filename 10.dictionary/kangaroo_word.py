source_word = "CHICKEN"

target_word = "HEN"

word_count = {}




for c in source_word:
    if c in word_count:
        word_count[c] += 1
    else:
        word_count[c] = 1

curr_index = 0
is_kangaroo_word = True

for ch in target_word:
    if ch in word_count and word_count.get(ch) > 0:
        word_count[ch] -= 1
    else:
        is_kangaroo_word = False
        
print(is_kangaroo_word)