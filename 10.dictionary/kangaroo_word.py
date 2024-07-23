source_word = "CHICKEN".lower()

target_word = "chi".lower()

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
        curr_index = source_word.find(ch, curr_index)
        if curr_index == -1:
            is_kangaroo_word = False
            break
        word_count[ch] -= 1
        curr_index += 1
    else:
        is_kangaroo_word = False
        break
    
print(is_kangaroo_word)