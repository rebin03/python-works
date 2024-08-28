# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A

def grade(mark):
    
    if mark > 80:
        return "A"
    elif mark >= 60:
        return "B"
    elif mark >= 50:
        return "C"
    elif mark >= 45:
        return "D"
    elif mark >= 25:
        return "E"
    else:
        return "F"
    
mark = int(input("Enter your mark: "))
print(f"Your grade is: {grade(mark)}")