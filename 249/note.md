##  自己的思路

- 首先写一个函数判断是否是 shift 数
    ```Python
    def is_shift(self,a,b):
        if not a or not b or len(a) != len(b):
            return False
       
        if len(a) == 1 and len(b) == 1:
            return True
        
        base = (ord(a[0]) - ord(b[0])) % 26
        
        for char_a,char_b in zip(a,b):
            if (ord(char_a) - ord(char_b))%26 != base:
                return False
            
        return True
    ```
    - a,b 中有一个为空，以及 a,b长度不相等返回False
    - a,b 长度都为1一定为 True
    - 再逐个比较a,b中字符的差(模)，如果所有的数对差都相等，则返回True

- 然后求 strings 集合里有多少个相等的集合
    - 每遇到一个新的string, 与已有集合中的key比较
    - 如果与某个key相等，加入到它的 value 数组里
    - 如果与所有的key都不相等，创建一个新的key和 value数组


## 最优思路
- 将每个字符串都转换成减去字符串首字符之后的字符串，这样所有 shift 字符串就有相同的key
```Python
def transform(self,a):
    def func(char,base = a[0]):
        return chr((ord(char) - ord(base))%26 + ord('a'))
    return "".join(map(func,a)) 
```

- 然后遍历一遍 strings 集合就可以把所有的子集合找出来
```Python
table = {}       
for string in strings:
    num = self.transform(string)
        if num not in table:
            table[num] = [string]
        else:
            table[num].append(string)
```
