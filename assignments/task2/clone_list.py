# Using slicing
def clone_by_slicing(lst):
    
    copy_lst = lst[:]
    
    return copy_lst

# Using assignment
def clone_by_assignment(lst):
    
    copy_lst = lst
    
    return copy_lst

# Using extend() method
def clone_by_extend(lst):
    
    copy_lst = []
    copy_lst.extend(lst)
    
    return copy_lst

# Using list comprehension
def clone_by_listComprehension(lst):
    
    copy_lst = [item for item in lst]
    
    return copy_lst

# Using append() method
def clone_by_append(lst):
    
    copy_lst = []
    
    for item in lst:
        copy_lst.append(item)
        
    return copy_lst

# Using copy() method
def clone_by_copy(lst):
    
    copy_lst = lst.copy()
    
    return copy_lst

# Using map function
def clone_by_map(lst):
    
    copy_lst = list(map(int, lst))
    
    return copy_lst


lst = [4, 8, 2, 10, 15, 18]

print(f"Original list: {lst}")

print(clone_by_slicing(lst))
print(clone_by_append(lst))
print(clone_by_assignment(lst))
print(clone_by_copy(lst))
print(clone_by_listComprehension(lst))
print(clone_by_map(lst))

