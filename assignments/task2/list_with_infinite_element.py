# yield keyword is used to create a generator function. A type of function that is memory efficient and can be used like an iterator object.

def infinite_list():
    
    n = 1
    
    while True:
        yield n
        n += 1
        

infinite_generator = infinite_list()

print(type(infinite_generator)) # this is an object of class generator

n = int(input("Enter the number of element to print from infinite list:\n"))

# Get the first n elements from the infinite list
for i in range(n):
    print(next(infinite_generator))