# Break a list into chunks of size N in Python

my_list = ['hello', 'for', 'hey', 'like',
           'come','python', 'django', 'this',
               'type','words', 'life']

def divide_chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]
        
        
n = 2

x = list(divide_chunks(my_list, n))
print(x)