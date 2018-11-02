"""
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.
"""





class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        
        trie = self.trie
        for c in word:
            trie = trie.setdefault(c,{})
        trie["#"] = "#"            

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        flag = False
        
        def recursive(word,trie):
            nonlocal flag
            
            if word == "" and "#" in trie:
                flag = True
                return          
            ## 单词过长
            if word != "" and trie == {"#":"#"}:
                return

    
            if word[0] == ".":
                for key in trie:
                    recursive(word[1:],trie[key])
                    
            elif word[0] in trie:
                recursive(word[1:],trie[word[0]])
            ## 不存在该前缀
            else:
                return

        recursive(word,self.trie)
        return flag
        
        
                
                
                
        
                
                
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)