vehicle_numbers = ["KL57X0297","KL07C5646","KL11C2458","KL12U6543"]

f = open("E:\\LUMINAR\\PythonJuneWorks\\15.file_programs\\vehicle_nums.txt","w")

for v in vehicle_numbers:
    f.write(v + "\n")