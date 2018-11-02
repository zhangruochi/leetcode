"""
In English, we have a concept called root, which can be followed by some other words to form another longer word - let's call this word successor. For example, the root an, followed by other, which can form another word another.

Now, given a dictionary consisting of many roots and a sentence. You need to replace all the successor in the sentence with the root forming it. If a successor has many roots can form it, replace it with the root with the shortest length.

You need to output the sentence after the replacement.

Example 1:

Input: dict = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
Note:

The input will only have lower-case letters.
1 <= dict words number <= 1000
1 <= sentence words number <= 1000
1 <= root length <= 100
1 <= sentence words length <= 1000
"""
class Solution:
    def create_trie(self,dict):
        trie = {}
        for root in dict:
            tmp_trie = trie
            for char in root:
                tmp_trie = tmp_trie.setdefault(char,{})
            tmp_trie["#"] = "#"
        return trie

    
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