def swap_first_and_last(lst):
    
    lst[0], lst[-1] = lst[-1], lst[0]
    
    return lst


lst = [4, 8, 2, 10, 15, 18]

print(swap_first_and_last(lst))