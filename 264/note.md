## 思路一

- An ugly number must be multiplied by either 2, 3, or 5 from a smaller ugly number.
- Assume you have Uk, the kth ugly number. Then Uk+1 must be Min(L1 * 2, L2 * 3, L3 * 5).


- 丑陋数的序列由它里面的数字乘以2，3，5得到。
- 因为数据需要按顺序增长，可以用三个指针保存需要乘以2,3,5的数字的位置。
- 每次选出最小数，并把该指针加1。



## 思路二
- 维护一个堆，每次弹出的数是当前最小的丑陋数
- 弹出的数的2，3，5倍都加入堆中，如果已经在堆中，则不加入。
- 用一个 count 记录当前是第几次弹出，第 n 次弹出的数即为所求。