## 思路

- 先进行层次遍历，用 table 记录每个 node 的 level，相同level 的node 放入同一个list
- level 为偶数的 list 需要倒转