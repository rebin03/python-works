def generator():
    
    print("First result:")
    yield 20
    
    print("Second result:")
    yield 30
    
    print("Third result:")
    yield 40
    

gen = generator()

print(next(gen))
print(next(gen))
print(next(gen))