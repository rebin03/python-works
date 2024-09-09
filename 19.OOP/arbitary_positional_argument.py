
class Operation:
    
    def perform_add(self, *args):
        
        total = sum([arg for arg in args if isinstance(arg, (int, float)) and not isinstance(arg, (bool))])
        return total
    
    def get_max_num(self, *args):
        return max(args)
    
    
math = Operation()

print(math.perform_add(10, 20))
print(math.perform_add(10, 20, 30, 30.5, "hello",True))

