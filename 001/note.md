## 思路
- 用一个 hashtable 存储 num 和 相应的 index.
- 遍历一遍数组，对相应的 num，查找 target-num 是否存在于 hashtable 中.
- 注意题目的条件是两个不相同的数，因此 index 不相等 

** if key in table ** 时间复杂度为 O(1). 因为 hashtable实际是一个巨大的稀疏数组， 针对每一个key先求散列值，散列值即为在该元素在稀疏数组中的偏移。

** if item in set ** 同理，set 背后也是用hashtable为底层