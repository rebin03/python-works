# Program to read student name and 3 marks mark1, mark2, mark3 and print total mark and avarage mark

student_name = input("Enter student name: ")
mark1 = input("Enter mark 1: ")
mark2 = input("Enter mark 2: ")
mark3 = input("Enter mark 3: ")

total_mark = int(mark1) + int(mark2) + int(mark3)

avg_mark = total_mark/3

print(f"{student_name}'s Total mark is {total_mark} and Average mark is {avg_mark}")