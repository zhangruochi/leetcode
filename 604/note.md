## 思路

"L     1     e   2   t   1C1o1d1e1"
 |     |     |
 char  num  Position

- 使用一个变量num保存当前字符的个数,使用一个变量position保存下一个字符的位置
- 每次调用 next, 返回当前字符，同时 num - 1. 
- 当 num == 0时， string 已到 position 位置，更新 num.