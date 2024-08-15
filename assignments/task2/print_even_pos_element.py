def display_even_pos_element(arr):
    
    for i in range(len(arr)):
        
        if i%2 != 0:
            print(arr[i])
            
            
arr = input().split()
display_even_pos_element(arr)