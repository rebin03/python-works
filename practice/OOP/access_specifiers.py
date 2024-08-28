class Student:
    
    def __init__(self, name, roll_no, age):
        self.name = name            # Public instance variable
        self._roll_no = roll_no     # Protected instance variable
        self.__age = age            # Private instance variable
        
    # provate member fuction
    def __display(self):
        print(f"I'm {self.name} {self.__age} year old with roll number {self._roll_no}")
        
    def displayPrivateData(self):
        self.__display()
        
class Brach(Student):
    def showProtectedData(self):
        print(f"My roll number is {self._roll_no}")

b1 = Brach("Alen", 33, 23)

# accessing public member
print(b1.name)

# object can also access protected member.(But it is better to not access protected members publicly outside the derived class)
print(b1._roll_no)

# Cannot access the private members (shows error: 'Brach' object has no attribute '__age')
# print(b1.__age)

# access protected within derived class public method
b1.showProtectedData()

# access private member through public method within the class
b1.displayPrivateData()

# But we can also access private members outside the class using 'name mangling' - use dir() fuction to find the mangled names
print(dir(b1))

# accessing private member
print(b1._Student__age)

# accessing private method
b1._Student__display()

