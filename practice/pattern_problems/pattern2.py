n = 5
for row in range(1,2*n):
    
    if row<=n:
        for col in range(1,row+1):
            print("*", end=" ")
    else:
        for col in range(2*n-row):
            print("*", end=" ")
            
    print()
    
    
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 