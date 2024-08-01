f = open("E:\\LUMINAR\\PythonJuneWorks\\15.file_programs\\news.txt","r")

words = [w for line in f for w in line.rstrip("\n").split(" ") if w != ""]

word_count = {word:words.count(word) for word in words}

srt = sorted(word_count, key=lambda key:word_count.get(key), reverse=True)

count = word_count.get(srt[0])

lst = [k for k,v in word_count.items() if v==count]
print(lst)