# Yield the square of a number
def squared_sequence(n):
    for x in range(n):
        yield x**2
        
        
        
generator = squared_sequence(5)

for sqr in generator:
    print(sqr)