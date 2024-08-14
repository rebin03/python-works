def grade_classification(percentage):
    
    if percentage >= 90:
        print("Grade A")
    elif percentage >=80:
        print("Grade B")
    elif percentage >=70:
        print("Grade C")
    else:
        print("Fail")
        
p = int(input("Enter percentage: "))
grade_classification(p)