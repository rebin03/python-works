def merge_the_tools(string, k):
    
    start = 0
    end = k
    
    while end <= len(string):
        
        temp = string[start:end]
        chunk = sorted(list(set(list(temp))), key=temp.index)
        
        print(''.join(chunk))
        
        start += k
        end += k
    
    
    

string, k = input(), int(input())
merge_the_tools(string, k)