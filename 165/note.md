## 自己的思路
- split(".") 变为字符串数组
- map(int, iterable) 变为数字数组
- 以较长的数组为迭代的次数,在比较重，超出较短数组的长度部分，给较短数组补0然后比较


## 别人的思路 
```Python
from itertools import zip_longest
```
- zip_longest 可以同时迭代两个对象, 用fillvalue给较短对象补足与较长对象所差的部分
