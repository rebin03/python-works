alph = 65
n = 10
for row in range(0,n):
    print(" " * (n-row), end=" ")
    for col in range(0,row+1):
        print(chr(alph), end=" ")
        alph += 1
    alph = 65
    print()
    


#       A 
#      A B
#     A B C
#    A B C D
#   A B C D E