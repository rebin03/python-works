class ComplexNumber:
    def __init__(self, r, i):
        self.real = r
        self.imaginary = i
        
    def __add__(self, other):
        return f"{self.real + other.real} + {self.imaginary + other.imaginary}i"
        
c1 = ComplexNumber(1, 2)
c2 = ComplexNumber(4, 5)
print(c1 + c2)