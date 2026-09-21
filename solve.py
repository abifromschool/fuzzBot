#Trie setup for boggle solver.

class Trie:
    def __init__(self):
        self.children = {}
        self.is_word = False

    def insert(self, word):
        node = self
        for letter in word:
            if letter not in node.children:
                node.children[letter] = Trie()
            node = node.children[letter]
        node.is_word = True

    def search(self, word):
        node = self
        for letter in word:
            if letter not in node.children:
                return False
            node = node.children[letter]
        return node.is_word


if __name__ == "__main__":
    t = Trie()
    for word in ["cat", "car", "card", "cards", "dog"]:
        t.insert(word)

    print(t.search("cat"))     # True
    print(t.search("car"))     # True
    print(t.search("card"))    # True
    print(t.search("ca"))      # False (prefix, not a word)
    print(t.search("cats"))    # False (not inserted)
    print(t.search("xyz"))     # False (letters not in trie at all)