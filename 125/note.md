## 自己的思路
- string.split(sbstring) 只能根据sbstring来分割字符.
- string.split(s[, sep[, maxsplit]]). If the optional second argument sep is absent or None, the words are separated by arbitrary strings of whitespace characters (space, tab, newline, return, formfeed)
- re.split(pattern,s) 可以根据pattern来分割字符串.
- \W+ 任意个非单词字符
- 回文字符串即s = s[::-1]

## 不借助外部函数
- 对字符串的清洗，可以遍历字符串，对每个字符进行判断是否是单词字符(根据ascii码的大小).
- 头尾字符比较，如果头尾出现不相等的字符，则不是回文字符串.