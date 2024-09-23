class NumberIter:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
    
iter_obj = NumberIter()

new_iter = iter(iter_obj)

for i in new_iter:
    print(i)