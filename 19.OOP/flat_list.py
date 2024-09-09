def flat_list(*args):
    
    lst = []
    
    for arg in args:
        
        if isinstance(arg, (list,)):
            lst.extend(flat_list(*arg))
        else:
            lst.append(arg)
    return lst


print(flat_list(1, 2, [10, 20], [10,[100, 200]]))