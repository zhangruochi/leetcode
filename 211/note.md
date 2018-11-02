## 思路

- 因为"."的存在需要递归当前 trie 下所有 key, 所以使用递归实现
- 递归出口为:
    - word搜索完毕，trie中存在"#"单词结束标志，说明搜索成功
    - word还未搜索完毕，但是 trie 已经到达结尾，说明单词过长，搜索失败
- 递归过程:
    - 如果当前字符为".",递归所有不为"#"的key
    - 如果当前字符在trie中，递归当前字符
    - 如果不在trie中，搜索失败，返回


```Python
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
```