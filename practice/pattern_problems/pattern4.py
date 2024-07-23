n = 5
for i in range(1,n+1):
    print(" "*(n-i), end="")
    
    for j in range(i,2*i):
        print(j, end="")
        
    for j in range(2*i-2, i-1, -1):
        print(j, end="")
    
    print()
    
    
#     1
#    232
#   34543
#  4567654
# 567898765