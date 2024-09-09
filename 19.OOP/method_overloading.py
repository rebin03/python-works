
class Operation:
    
    def perform_add(self, *args):
        return sum(args)
    
    def get_max_num(self, *args):
        return max(args)
    
    
math = Operation()

print(math.perform_add(10, 20))
print(math.perform_add(10, 20, 30))