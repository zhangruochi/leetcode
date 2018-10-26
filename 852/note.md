## 思路
- 二分查找的关键是看能否找到折半条件
- 对于 mountain 数列，如果存在 连续三个数递增的情况 A[mid+1] > A[mid] and A[mid] > A[mid-1], 此时 mid+1 位置以前的数都不用看了
- 如果存在 连续三个数递减的情况 A[mid-1] > A[mid] and A[mid] > A[mid+1], 此时 mid-1 位置以前的数都不用看了