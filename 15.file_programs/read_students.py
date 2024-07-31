f = open("E:\\LUMINAR\\PythonJuneWorks\\15.file_programs\\students.txt","r")

students = []

for stud in f:
    students.append(stud.rstrip("\n"))

print(students)