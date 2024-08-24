# anagram - charecters in source word is same as in target word. count should be equal

source_word = "listen"
target_word = "silent"

def is_anagram(source_word, target_word):
    
    sorted_str1 = sorted(source_word)
    sorted_str2 = sorted(target_word)
    
    return True if sorted_str1 == sorted_str2 else False


print(is_anagram(source_word, target_word))