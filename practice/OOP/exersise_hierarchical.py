class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def sleep(self):
        print("I can sleep")
        
    def display(self):
        print(f"I'm {self.name}, {self.age} year old.", end=" ")
        
class Faculty(Person):
    
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
        
    def work(self):
        print("I can teach")
        
    def display(self):
        super().display()
        print(f"I can teach {self.subject}")
        
class Student(Person):
    
    def __init__(self, name, age, like_subject):
        super().__init__(name, age)
        self.like_subject = like_subject
        
    def work(self):
        print("I can code")
        
    def display(self):
        super().display()
        print(f"My favourite subject is {self.like_subject}")
        
        
faculty = Faculty("Jane", 30, "Python")
faculty.display()

student = Student("Aman", 18, "Maths")
student.display()