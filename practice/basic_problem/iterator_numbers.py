class NumberIter:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x
    
iter_obj = NumberIter()

new_iter = iter(iter_obj)

print(next(new_iter))
print(next(new_iter))
print(next(new_iter))
print(next(new_iter))