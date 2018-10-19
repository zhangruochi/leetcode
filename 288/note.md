##  思路

- 如果两个单词s,t缩写相等，则 s[0] == t[0] and s[-1] == t[-1] and len(s) = len(t)
- 可以对于输入的单词，和字典里所有的单词都进行这样的比较。
- 但是如果要比较n个单词，时间复杂度就为O(n^2)

## 改进思路

- 对输入的单词建立一个HashTable, key为词的缩写， value为一个list, 保存着所有缩写为 key 的 word
- 对于需要检查的单词 word,有以下几种情况：
    - word 的缩写不在HashTable里，返回True
    - word 的缩写 key 在 HashTable 里，但是 len(HashTable[key]) >= 2, 返回 False
    - len(HashTable[key]) == 1,  判断唯一的单词是否与 word 相等


## 最优思路
```Python
for word in dictionary:
    trans_word = self.transform(word)
    if trans_word not in self.dictionary:
        self.dictionary[trans_word] = word
    else:
        self.dictionary[trans_word] = False
```
- 在建立HashTable时，当某个单词出现第一次时，key = 缩写，value = word，第二次出现时，直接置为False 