## 思路
- 用一个table记录每个元素的个数
- 重新遍历一遍 string，遇到第一个数量等于1的元素就返回
- 没有该元素，返回-1

## 最优思路
- 可以用数组记录每个元素的个数,空间复杂度更低
```Python
table = [0]*26
for char in s:
    table[ord(char)-ord('a')] += 1
```