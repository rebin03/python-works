student_mark = {
    "Jenny":92,
    "Harry":78,
    "Dimpy":56,
    "Rahul":41,
    "Aniket":99,
    "Prem":34
}

student_grades = {}

for name in student_mark:
    
    mark = student_mark[name]
    
    if mark > 90:
        
        student_grades[name] = "A+"
        
    elif mark > 80:
        
        student_grades[name] = "A"
        
    elif mark > 70:
        
        student_grades[name] = "B+"
    
    elif mark > 60:
        
        student_grades[name] = "B"
    
    elif mark > 50:
        
        student_grades[name] = "C"
        
    elif mark > 40:
        
        student_grades[name] = "D"
    
    else:
        
        student_grades[name] = "F"
        
print(student_grades)
        
        