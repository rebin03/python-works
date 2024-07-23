studend_data = [
    {
        "name":"Ram",
        "roll_no":10,
        "age":20,
        "course":"Python"
    },
    {
        "name":"Mohan",
        "roll_no":20,
        "age":22,
        "course":"Java"
    }
]


def add_new_student(name, roll_no, age, course):
    
    studend_data.append({"name":name, "roll_no":roll_no, "age":age, "course":course})
    
add_new_student("Rebin", 35, 22, "Python")
print(studend_data)