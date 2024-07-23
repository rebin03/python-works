student = {"name":"hari", "course":"data science", "place":"chennai"}

for key in student:
    if key == "course":
        student[key] = "fullstack"
        
print(student)