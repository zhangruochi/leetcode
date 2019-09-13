## 思路
- 中序遍历BST,得到递增序列
- 采用两端夹逼的方法得到 sum == low + high (参考 two sum II)


## 最有思路

- 中序遍历，同时用set保存已遍历的值，查找 target - 当前值是否存在于 set 中