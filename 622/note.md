## 思路

- 使用 front 和 tail
- front 始终指向 queue 的第一个元素
- tail 始终指向 queue 的第一个空位置
- 如果 front  == tail 且 queue[front]  不为空，则说明队列已满
- 如果 front  == tail 且 queue[front]  为空，则说明队列已空