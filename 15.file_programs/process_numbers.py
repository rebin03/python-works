
f_read = open("E:\\LUMINAR\\PythonJuneWorks\\15.file_programs\\numbers.txt","r")
f_odd = open("E:\\LUMINAR\\PythonJuneWorks\\15.file_programs\\odd.txt","w")
f_even = open("E:\\LUMINAR\\PythonJuneWorks\\15.file_programs\\even.txt","w")

for num in f_read:
    
    n = int(num.rstrip("\n"))
    
    if n%2 == 0:
        
        f_even.write(str(n) + "\n")
        
    else:
        
        f_odd.write(str(n) + "\n")