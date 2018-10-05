## 自己的思路

1.     1
2.     11
3.     21
4.     1211
5.     111221

- 根据规律，需要用一个 count 变量保存当前 number 中相同 digit 的个数. 用一个 prev 保存当前的 digit. 
- 遇到不相等的 digit, 就把 str(count) + prev 添加到 result string 里面， 然后把 prev 修改为当前的 digit, count 修改为 1
- 对于相同的digit，只需要将 count + 1
