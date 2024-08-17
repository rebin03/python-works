def is_nth_element_exist(lst, n):
    
    return len(lst) > n

lst = [4, 8, 2, 10, 15, 18]

n = int(input("Enter n-th index: "))
print(f"Is nth index available? : {is_nth_element_exist(lst, n)}")