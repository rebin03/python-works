# Python doesn't support method overloading by default.
# To achieve this we need to use default default argument or arbitary argument(*args)
# Method overloading is compile time polymorphism. because, with the help of no. of argument passed the the appropriate method to be called will be decided.
# Mthod overloading occures within the same class.
# it must have same method name but with different number of parameter.

class Demo:
    # To overload method adding default parameter equal to 0. this will achive method overloading
    def add(self, a, b, c=0):
        return a+b
    
    # If the number of arguments is unknown, then we can use *args parameter. here we can pass any number of arguments
    def add_no(self, *args):
        res = 0
        for i in args:
            res += i
        return res
    
    # we can't overload methods like this in python. this will actually override the previous methos and will show error if previous method was called.
    # def add(self, a, b, c):
    #     return a+b+c

d = Demo()
print(d.add(4, 6))
print(d.add(1, 2, 3))

print(d.add_no(4, 6, 3, 5, 1))