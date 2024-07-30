lst = [10,11,12,15,10,12,15,11,13,14,15,10]

number_count = {n:lst.count(n) for n in lst}
print(number_count)

#---------------------------------------------------------------------------------------------------------

words = ["hello","hai","hello","hai","hello"]

word_count = {w:words.count(w) for w in words}
print(word_count)

#---------------------------------------------------------------------------------------------------------

# in case of text
text = "hello hai hello hai hello"
words1 = text.split(" ")

word_count = {w:words1.count(w) for w in words1}
print(word_count)
