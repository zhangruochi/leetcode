"""
Given a list of strings words representing an English Dictionary, find the longest word in words that can be built one character at a time by other words in words. If there is more than one possible answer, return the longest word with the smallest lexicographical order.

If there is no answer, return the empty string.
Example 1:

Input: 
words = ["w","wo","wor","worl", "world"]
Output: "world"
Explanation: 
The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
Example 2:

Input: 
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
Output: "apple"
Explanation: 
Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".
Note:

All the strings in the input will only contain lowercase letters.
The length of words will be in the range [1, 1000].
The length of words[i] will be in the range [1, 30].
"""

class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        res = ""
        
        trie = {}
        for word in words:
            tmp_trie = trie
            for char in word:
                tmp_trie = tmp_trie.setdefault(char,{})
            tmp_trie["#"] = "#"
            
        
        def update(path):
            nonlocal res
            if len(path) > len(res) or (len(path) == len(res) and path < res):
                res = path
            

        def dfs(trie,path):
            
            if "#" in trie:
                update(path)
                
            for char in trie:
                # 剪枝
                if "#" not in trie[char] or char == "#": 
                    continue
            
                dfs(trie[char], path + char)
                
        dfs(trie,"")
        
        return res