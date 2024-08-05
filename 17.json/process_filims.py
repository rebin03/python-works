from json import load
f = open("E:\\LUMINAR\\PythonJuneWorks\\17.json\\films.json","r")

movies = load(f)

for mov in movies:
    print(mov.get("title"))