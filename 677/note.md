## 思路

- 难点在sum 的实现
- 如果不存在前缀，返回0
- 如果存在前缀，判断每一步是否存在单词，即是否有单词标识，如果有，total 加上 value
- 然后把以该前缀所有下一种可能的情况递归过去。

```Python
def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        total = 0
        trie = self.trie
        for c in prefix:
            if c not in trie:
                return total
            trie = trie[c]
        
        def recursive(trie):
            nonlocal total
            for char in trie:
                if char == "#":
                    total += trie["#"]
                else:
                    recursive(trie[char])
        
        recursive(trie)
        return total
```