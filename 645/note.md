## 自己的思路
建立一个 key 为所有会出现的整数，value为 0 的 Hashmap.  遍历给定的nums, 利用 Hashmap 记录所有数字出现的次数。最后返回出现次数为2和0的。

## 空间复杂度为0（1）的思路

- 数字最多只会出现出现两次，可以用一位来记录信息。
- 遍历数组，将每一个数字（绝对值）对应的位置的数据变为其相反数。
- 如果该位置的数字已经为负数，说明为第二次出现。
- 最后再遍历一遍数组，仍然为正的数字的位置即为一次都没有出现的数字。