class MinMaxWordFinder:
    def __init__(self):
        self.words = []

    def add_sentence(self, sentence):
        words = [word.strip(".,!?;:()\"'") for word in sentence.split()]
        self.words.extend(word for word in words if word)

    def shortest_words(self):
        if not self.words:
            return []
        min_length = min(map(len, self.words))
        shortest = [word for word in self.words if len(word) == min_length]
        return sorted(shortest)

    def longest_words(self):
        if not self.words:
            return []
        max_length = max(map(len, self.words))
        longest = {word for word in self.words if len(word) == max_length}
        return sorted(longest)