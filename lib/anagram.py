# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = sorted(word)

    def match(self, possible_anagrams):
        matches = []
        for candidate in possible_anagrams:
            if candidate != "".join(self.word) and sorted(candidate) == self.word:
                matches.append(candidate)
        return matches

    