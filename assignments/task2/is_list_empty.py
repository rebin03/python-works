def is_list_empty(lst):
    
    return len(lst) == 0


lst = [2,6,9]
print("list is empty" if is_list_empty(lst) else "list is not empty")