def display_odd_pos_element(arr):
    
    for i in range(len(arr)):
        
        if i%2 == 0:
            print(arr[i])
            
            
arr = input().split()
display_odd_pos_element(arr)