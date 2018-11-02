##  思路
- 前缀树的应用
- 要判断句子里每个单词是否含有某个前缀
- 暴力解法: 遍历每个单词，对每个单词再遍历前缀，这样时间复杂度为O(n^2)
- 利用前缀树的解法:
    - 先把所有前缀构造成前缀树
    ```Python
    def create_trie(self,dict):
        trie = {}
        for root in dict:
            tmp_trie = trie
            for char in root:
                tmp_trie = tmp_trie.setdefault(char,{})
            tmp_trie["#"] = "#"
        return trie
    ```
    - 然后遍历每个单词，对每个单词在前缀树里搜索(相当于一次搜索可以判断所有前缀)，时间复杂度为O(n)
    ```Python
    def search(self,trie,word):
        prefix = ""
        for c in word:
            if c not in trie:
                return word
            trie = trie[c]
            prefix += c
            if "#" in trie:
                return prefix
        return word
        
        
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        trie = self.create_trie(dict)
        word_list = []
        for word in sentence.split():
            word_list.append(self.search(trie,word))
        return " ".join(word_list)
    ```