# sample input:
#     PQR
#     ABC
# Output:
#     PAQBRC

word1 = "PQRST"
word2 = "ABC"
word = ""


smallest_word = word1 if len(word1) < len(word2) else word2

for i in range(0,len(smallest_word)):
    word = word+word1[i]+word2[i]

if len(word1) < len(word2):
    
    word = word + word2[len(word1):len(word2)+1]
    
else:
    
    word = word + word1[len(word2):len(word1)+1]
        

               
print(word)