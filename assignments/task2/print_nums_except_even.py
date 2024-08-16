def remove_even(lst):
    
    res = [num for num in lst if num%2 != 0]
    return res


lst = [4, 7, 8, 9, 2, 5, 10, 15, 18, 19]

print(remove_even(lst))