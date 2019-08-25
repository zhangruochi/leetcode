## 思路

###  自己的思路
- 使用set作为底层数据结构，可以支持O(1)的insert或remove；
- set不支持索引，所以将set转化为list；
- 为了得到均分分布的随机数，使用randint函数
```python
random.randint(a,b)
# Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).
```


### 别人的思路

- 使用 table 保存 num 和 index
- 使用 list 保存 num
- 删除时，交换数组最后一个元素和需要删除的元素，同时删除最后一个元素。