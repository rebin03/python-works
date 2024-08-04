def print_rangoli(size):
    alphabets = [chr(i) for i in range(97, 123)]
    alphabets = alphabets[:size]
    
    indices = list(range(size))
    indices = indices[:-1] + indices[::-1]
    
    for i in indices:
        start_index = i + 1
        original = alphabets[-start_index:]
        reverse = original[::-1]
        row = reverse + original[1:]
        row = "-".join(row)
        width = size * 4 - 3
        row = row.center(width, "-")
        print(row)
    
        
    

n = 3
print_rangoli(n)