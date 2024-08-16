import random

def shuffle_list(lst):
    
    random.shuffle(lst)
    
    return lst


lst = [4, 8, 2, 10, 15, 18]

print(shuffle_list(lst))