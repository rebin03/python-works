class TopTen():
    
    def __init__(self):
        self.num = 1
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.num <= 10:          # In the __next__() method, we can add a terminating condition to raise an error if the iteration is done a specified number of times
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration     # To prevent the iteration from going on forever, we can use the StopIteration statement.
                                    
    

iterable = TopTen()

iterator = iter(iterable)

print(next(iterator))

for i in iterable:
    print(i)