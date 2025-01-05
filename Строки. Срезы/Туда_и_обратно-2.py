word = input()
word2 = ''
for i in word:
    if i == ' ':
        continue
    else:
        word2 += i
        
print(word2 == word2[::-1])