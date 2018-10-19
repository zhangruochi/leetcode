## 思考
- 逆转180°还相等的数为 0,1,6,9,8
- 利用一个 hashtable 保存互相的映射关系
```Python
dict_table = {"6":"9","9":"6","8":"8","1":"1","0":"0"}
```

- 从左右两段分别比较对应的字符，左边在 table中找映射，遇到和右边不相等的情况就返回False
```Python
for i in range(len(num)//2+1):
    if num[i] not in dict_table or dict_table[num[i]] != num[-i-1]:
        return False
```