## 思路

- 创建一个数据结构，table = defaultdict(set), key 为字符， val为一个集合，元素为字符的索引以及该字符(index,char)
- 对secret和guess都求上述 table 
- 对于某个字符，位置相同的字符数量即为 两个 val 集合的交集
- 位置不同的字符的数量为 数量较少集合减去交集

```Python
for key,guess_set in guess_table.items():
            if key in secret_table:
                same = guess_set & secret_table[key]
                count_A += len(same)
                count_B += min(len(guess_set-same),len(secret_table[key]-same))
```

## 最优思路

- 计算每个字符串中不同字符出现的次数
- 同时遍历一遍两个字符串，找出相同位置的字符，并在总次数中减去相同位置的字符
- 不同 counter 中，相同字符较小的 val 即为不同位置的字符数量

```Python
from collections import Counter
class Solution:
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        count_s = Counter(secret)
        count_g = Counter(guess)
        
        count_a = 0
        for s,g in zip(secret,guess):
            if s == g:
                count_a += 1
                count_s[s] -= 1
                count_g[g] -= 1
        
        count_b = 0
        for char in count_g:
            if char in count_s:
                count_b += min(count_g[char],count_s[char])
        
        return "{}A{}B".format(count_a,count_b)
```