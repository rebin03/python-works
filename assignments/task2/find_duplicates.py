def get_duplicate_elements(arr):
    
    element_count = {}
    
    for el in arr:
        
        if el in element_count:
            element_count[el] += 1
        else:
            element_count[el] = 1
            
    dup_list = [key for key, value in element_count.items() if value > 1]
    
    # for key, value in element_count.items():
    #     if value > 1:
    #         dup_list.append(key)
            
    return dup_list


arr = list(input().split())
print(get_duplicate_elements(arr))