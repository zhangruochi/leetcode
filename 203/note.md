## 思路
- 为了方便跳过，cur.next = cur.next.next, 总是判断当前指针的下一个 node
- 因为第一个 node 可能就需要被删除, 用一个哨兵结点
- 遍历链表，遇到val相等直接跳过