## 思路

- 完全借用循环队列的实现思路
	- 队满  (tail + 1) % k == head
	- 队空  tail == head
