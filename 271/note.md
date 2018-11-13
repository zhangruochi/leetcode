## 思路

- 编码采用的方式为 str_length + "@" + str  的方式
- str_length 放在"@" 前面可以避免 str_length 与 str 开头的数字组成更大的数字
- str_length + "@" 然后再 根据 str_length 找到 str, 把 str 加入 ans 后从 strs中删除，这样可以避免其他 "@"的干扰