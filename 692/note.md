## 思路
- 用 hash table 计算每个 words 的 frequence
- 根据frequence对元素进行排序，如果frequence相等，使用 word 的字典顺序进行排序。
```
If two words have the same frequency, then the word with the lower alphabetical order comes first.
```
- 根据比较规则创建 Comparable 对象，然后使用内置的 sort 函数直接排序就好。