## 自己的思路
- 创建一个 values = [], 遍历链表，记录链表里所有的数.
- reverse 链表  Time Complexity = O(n)
- 同时比较链表和values里面的值，如何全部相等，返回 True
- Space Complexity = O(n)


## Space Complexity = O(1)
- 寻找链表的中点，用两个指针，分别是快指针和慢指针，快指针每次跳两格，慢指针每次跳一格。当快指针到终点时，慢指针正好到中点.
- 将中点后的链表reverse
- 比较中点开始的后段链表和起点开始的前端链表的值