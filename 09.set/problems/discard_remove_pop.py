n = int(input())
s = set(map(int, input().split()))
N = int(input())

for i in range(N):
    
    user_input = input().split()
    
    if len(user_input) == 1:
        command = user_input[0]
    else:
        command = user_input[0]
        val = int(user_input[1])
    
    if command == "pop":
        s.pop()
    elif command == "remove":
        s.discard(val)
    elif command == "discard":
        s.discard(val)
        
print(sum(s))