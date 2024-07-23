n= 5

for row in range(1, n+1):
    
    for col in range(row):
        print("*", end="")
    
    print(" " * (2 * (n-row)), end="")
    
    for col in range(row):
        print("*", end="")
    
    print()
    
    
# *        *
# **      **
# ***    ***
# ****  ****
# **********