## 思路
- stack的 pop() 是弹出最后一个元素， queue的 pop()是弹出第一个元素
- 新建一个 tmp_stack = [], 将 stack 的每一个元素弹出，最后一个元素保留最后返回. 然后再把 tmp_stack 中的元素 pop 回 stack
- 负负等正的思路