def up_to(n):
    for i in range(n):
        yield i
        

gen = up_to(5)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen))  #StopIteration