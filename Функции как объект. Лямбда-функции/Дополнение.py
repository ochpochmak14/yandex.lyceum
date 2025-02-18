words = input().split()
max_length = len(max(words, key=len))
formatted_words = map(lambda word: "*" * (max_length - len(word)) + word, words)
print(*formatted_words, sep="\n")
