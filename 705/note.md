## 思路

- hashset 本质上是一个巨大的稀疏数组，根据 key 来计算数组的下标，然后把value存在对应的 bucket中