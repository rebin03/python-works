def count_words(string):
    
    lst = string.split()
    count = len(lst)
    
    return count

string = input("Enter sentence: ")
print(count_words(string))