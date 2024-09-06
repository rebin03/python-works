class Person:
    
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def display(self):
        print(f"Name: {self.name}\nAge: {self.age}\nGender: {self.gender}")
        
        
class Employee(Person):
    
    def __init__(self,name, age, gender, eid, department, salary):
        super().__init__(name, age, gender)
        self.eid = eid
        self.department = department
        self.salary = salary
        
    def display(self):
        super().display()
        print(f"EID: {self.eid}\nDepartment: {self.department}\nSalary: {self.salary}") 
        
        
emp1 = Employee("John", 34, "Male", 12345, "IT", 45000)
emp1.display()