from re import fullmatch

f = open("E:\\LUMINAR\\PythonJuneWorks\\18.RegEx\\domain.txt","r")
pattern = "[\\w\\W]+\\.com"

for domain in f:
    domain = domain.rstrip("\n")
    matcher = fullmatch(pattern, domain)
    
    if matcher != None:
        print(domain)