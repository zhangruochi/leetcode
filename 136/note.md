### 自己的思路
先利用排序算法对数组进行排序，此处时间复杂度为 nlog(n)， 然后判断两两是否相等（最后一个元素除外）。若出现前后不相等的情况，必定为前者为 single number。
若没有两两不相等的情况，返回排序的最后一个数。


### 最优思路
直接对所有的数据进行xor 操作。因为满足交换律，所有相同的数对最终会得0. 


### 异或操作的重要特性
    - x^x = 0
    - x^1s = ~x
    - x^0s = x
    - 异或满足交换律

### reduce
```Python
from functools import reduce
reduce(function, iterable[, initializer])
reduce(add, [1,2,3,4,5]) #-> 15
```
函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：用传给 reduce 中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。

### xor
```Python
from operator import xor
```


