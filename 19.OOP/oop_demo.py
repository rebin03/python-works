class Student:
    name:str
    roll_no:int
    course:str
    age:int
    gender:str
    
    def __init__(self, name, roll_no, course, age, gender):
        self.name = name
        self.roll_no = roll_no
        self.course = course
        self.age = age
        self.gender = gender
        
    def display(self):
        print(f"Name: {self.name}\nRoll no: {self.roll_no}\nCourse: {self.course}\nAge: {self.age}\nGender: {self.gender}")
        

obj = Student("Rebin", 35, "Python", 22, "Male")

obj.display()