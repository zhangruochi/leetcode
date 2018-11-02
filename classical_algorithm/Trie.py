class Trie:
    def __init__(self):
        self.trie = {}
        self.size = 0

    def add(self, word):
        trie = self.trie
        word = word.strip()
        for c in word:
            trie = trie.setdefault(c,{})
        trie["#"] = "#"

    def search(self,word):
        trie = self.trie
        word = word.strip()
        for c in word:
            if not c in trie:
                return False
            trie = trie[c]
        if "#" in trie:
            return True
        return False


if __name__ == '__main__':
    trie_obj = Trie()
    trie_obj.add("hello")
    trie_obj.add("world")

    print(trie_obj.search("hello"))
    print(trie_obj.search("world"))
    print(trie_obj.search("zhang"))
