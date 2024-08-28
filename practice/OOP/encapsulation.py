class Student:
    
    def __init__(self, name, roll_no, age):
        self.name = name            # Public instance variable
        self._roll_no = roll_no     # Protected instance variable
        self.__age = age            # Private instance variable
        
    # provate member fuction
    def __display(self):
        print(f"I'm {self.name} {self.__age} year old with roll number {self._roll_no}")
        
    # getter method to access the private data '__age'
    def get_age(self):
        return self.__age
    
    # setter method to modify the private data '__age'
    def set_age(self, age):
        self.__age = age
        
    def displayPrivateData(self):
        self.__display()
        
class Brach(Student):
    def showProtectedData(self):
        print(f"My roll number is {self._roll_no}")

s1 = Student("Alen", 33, 23)

# In python, the best way to achieve encapsulation is by using getter and setter methods

# Accessing the private member using getter
print(s1.get_age())

# Modifiying the private member using setter
s1.set_age(45)

print(s1.get_age())