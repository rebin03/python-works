class University:
    
    def __init__(self, uni_name):
        self.uni_name = uni_name
    
    def show_detail(self):
        print(f"University: {self.uni_name}")
    
class Course(University):
    
    def __init__(self, uni_name, course_name):
        University.__init__(self, uni_name)
        self.course_name = course_name
        
    def show_detail(self):
        super().show_detail()
        print(f"Course: {self.course_name}")

class Branch(University):
    
    def __init__(self, uni_name, branch_name):
        University.__init__(self, uni_name)
        self.branch_name = branch_name
        
    def show_detail(self):
        super().show_detail()
        print(f"Branch: {self.branch_name}")

class Student(Branch, Course):
    
    def __init__(self, name, uni_name, course_name, branch_name):
        Course.__init__(self, uni_name, course_name)
        Branch.__init__(self, uni_name, branch_name)
        self.name = name
    
    def show_detail(self):
        print(f"Student name: {self.name}")
        super().show_detail()

class Faculty(Branch):
    
    def __init__(self, name, uni_name, branch_name):
        super().__init__(uni_name, branch_name)
        self.name = name
        
    def show_detail(self):
        print(f"Faculty name: {self.name}")
        super().show_detail()
        
        
john = Student("John", "Cambridge", "B.Tech", "CSE")
john.show_detail()

jenni = Faculty("Jenni", "CUSAT", "MCA")
jenni.show_detail()