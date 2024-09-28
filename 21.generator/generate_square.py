# Yield the square of a number
def squared_sequence(n):
    for x in range(n):
        yield x**2
        
        
        
gen_obj = squared_sequence(5)

while True:
    try:
        print("Recieved on next(): ", next(gen_obj))
    except StopIteration:
        break