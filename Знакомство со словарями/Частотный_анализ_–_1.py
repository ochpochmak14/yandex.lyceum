n = int(input()) 
text = ""
for _ in range(n):
    text += input() + " " 
symbols = ",.!?:;"
words = []
for word in text.split():
    clean_word = ''.join(char for char in word if char not in symbols)  
    if clean_word: 
        words.append(clean_word.lower())
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))

for word, count in sorted_words:
    print(word.capitalize())
